from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from datetime import datetime
from .models import Music, Video, Audio, Mixtape, Comments, AudioCount, VideoCount, Confirmemail, Lyrics, dont_eat_baby_food
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_decode
from django.http import Http404, HttpResponseRedirect
from Gist.models import GistPost
from News.models import NewsPosts
from django.db.models import Q
from Profile.models import ProfilePic
from django.http import Http404
from .forms import Addmusic, Addaudio, Addvideo, AddMixtape, EditMixtape, Editmusic, Editaudio, Editvideo
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from hitcount.views import HitCountDetailView
from django.views.generic import ListView

class PostCountHitDetailView(HitCountDetailView):
    model = Video        # your model goes here
    count_hit = True


def home(request):

    time = datetime.now()
    day = time.strftime("%A")
    hour = time.hour
    if hour < 12:
        message = "Good Morning"
    elif 12 <= hour < 16:
        message = "Good afternoon"
    else:
        message = "Good Evening"

    first_six = Music.objects.all().order_by('-id')[:6]
    first_twelve = Music.objects.all().order_by('-id')[6:9]

    print(first_six)
    context = {'time': time, 'message': message, 'day': day, 'first_six': first_six, 'first_twelve':first_twelve }
    template = 'Music/home.html'
    return render(request, template, context)

class debf(ListView):
    context_object_name = 'debf_list'
    template_name = 'Music/testes.html'
    queryset = dont_eat_baby_food.objects.all().order_by('-id')




def newsticker(request):
    template = 'Music/newsticker.html'
    return render(request, template)


def home1(request):
    #video
    first = Video.objects.all().filter(publish=True).order_by('-id')[:1]
    second = Video.objects.all().filter(publish=True).order_by('-id')[1:2]
    third = Video.objects.all().filter(publish=True).order_by('-id')[2:3]
    #forth = Music.objects.all().order_by('-id')[3:4]
    #first_twelve = Music.objects.all().order_by('-id')[6:9]
    first_ten_song = Audio.objects.all().filter(publish=True).order_by('-id')[3:11]
    videos = Video.objects.all().filter(publish=True).order_by('-id')[3:11]
    #from News
    first_slide = NewsPosts.objects.all().filter(publish=True).order_by('-id')[:1]
    second_slide = NewsPosts.objects.all().filter(publish=True).order_by('-id')[1:2]
    third_slide = NewsPosts.objects.all().filter(publish=True).order_by('-id')[2:3]
    forth_slide = NewsPosts.objects.all().filter(publish=True).order_by('-id')[3:4]
    fifth_slide = NewsPosts.objects.all().filter(publish=True).order_by('-id')[4:5]
    sixth_slide = NewsPosts.objects.all().filter(publish=True).order_by('-id')[5:6]
    news = NewsPosts.objects.all().filter(publish=True).order_by('-id')[6:9]

    #Gist
    slide0ne = GistPost.objects.all().filter(publish=True).order_by('-id')[:1]
    slidetwo = GistPost.objects.all().filter(publish=True).order_by('-id')[1:2]
    slidethree = GistPost.objects.all().filter(publish=True).order_by('-id')[2:3]
    slidefour = GistPost.objects.all().filter(publish=True).order_by('-id')[3:4]
    slidefive = GistPost.objects.all().filter(publish=True).order_by('-id')[4:5]
    slidesix = GistPost.objects.all().filter(publish=True).order_by('-id')[5:6]
    gist = GistPost.objects.all().filter(publish=True).order_by('-id')[6:9]
    #Songs
    one = Audio.objects.all().filter(publish=True).order_by('-id')[:1]
    two = Audio.objects.all().filter(publish=True).order_by('-id')[1:2]
    three = Audio.objects.all().filter(publish=True).order_by('-id')[2:3]

    #print(first_six)
    context = {'videos': videos, 'first': first, 'second': second, 'third': third, 'first_ten_song': first_ten_song,
               'first_slide': first_slide, 'second_slide': second_slide, 'third_slide': third_slide,
               'forth_slide': forth_slide, 'fifth': fifth_slide, 'sixth': sixth_slide, 'slideone': slide0ne,
               'slidetwo': slidetwo, 'slidethree': slidethree, 'slidefour': slidefour, 'one': one, 'two': two,
               'three': three, 'news': news, 'gist': gist, 'slidefive': slidefive, 'slidesix': slidesix}

    template = 'Music/home1.html'
    return render(request, template, context)


def testing(request):

    new = NewsPosts.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(new, 20)
    try:
        newss = paginator.page(page)
    except PageNotAnInteger:
        newss = paginator.page(2)
    except EmptyPage:
        newss = paginator.page(paginator.num_pages)
    context = {'newss': newss, 'new': new}
    template = 'Music/testing.html'
    return render(request, template, context)


def songs(request):
    song = Audio.objects.all().filter(publish=True).order_by('-id')
    paginator = Paginator(song, 20)
    page = request.GET.get('page', 1)
    try:
        songss = paginator.page(page)
    except PageNotAnInteger:
       songss = paginator.page(1)
    except EmptyPage:
        songss = paginator.page(paginator.num_pages)
    #second_songs = Audio.objects.all().order_by('-id')[12:]
    template = 'Music/songs.html'
    context = {'songss': songss}
    return render(request, template, context)


def gospel(request):
    first_fifteen_gospel = Audio.objects.all().filter(Q(music__genre='Christian/Gospel') | Q(music__genre='R&B/soul')
                                                      ).order_by('-id')[:15]
    template = 'Music/gospel.html'
    context = {'first_fifteen_gospel': first_fifteen_gospel}
    return render(request, template, context)


def hip_hop_rap(request):
    first_twelve_hip_hop_rap = Audio.objects.all().filter(music__genre='Hip-Hop/Rap').order_by('-id')[:12]
    second_hip_hop_rap = Audio.objects.all().filter(music__genre='Hip-Hop/Rap').order_by('-id')[12:]
    template = 'Music/hiphoprap.html'
    context = {'first_twelve_hip_hop_rap': first_twelve_hip_hop_rap, 'second_hip_hop_rap': second_hip_hop_rap}
    return render(request, template, context)

def hiphop_pop(request):
    hiphop_pop = Audio.objects.all().filter(Q(music__genre='Hip-Hop') | Q(music__genre='Pop')).order_by('-id')[:15]
    template = 'Music/hiphop-pop.html'
    context = {'hiphop_pop': hiphop_pop}
    return render(request, template, context)

def others(request):
    genres = ['Christian/Gospel', 'Hip-Hop/Rap', 'R&B/Soul', 'Hip-Hop', 'Pop']
    song_others = Audio.objects.all().filter(~Q(music__genre__in=genres)).order_by('-id')[:12]
    template = 'Music/song-others.html'
    context = {'song_others': song_others}
    return render(request, template, context)


def video(request):
    videos = Video.objects.all().filter(publish=True).order_by('-id')
    paginator = Paginator(videos, 20)
    page = request.GET.get('page', 1)
    try:
        all_video = paginator.page(page)
    except PageNotAnInteger:
        all_video = paginator.page(1)
    except EmptyPage:
        all_video = paginator.page(paginator.num_pages)

    template = 'Music/video.html'
    context = {'all_video': all_video}
    return render(request, template, context)


def video_gospel(request):
    vedeo_gospel = Video.objects.all().filter(Q(music__genre='Christian/Gospel') | Q(music__genre='R&B/soul')
                                                      ).order_by('-id')[:15]
    vedeo_gospel2 = Video.objects.all().filter(Q(music__genre='Christian/Gospel') | Q(music__genre='R&B/soul')
                                              ).order_by('-id')[15:]
    template = 'Music/video_gospel.html'
    context = {'vedeo_gospel':  vedeo_gospel, 'vedeo_gospel2': vedeo_gospel2}
    return render(request, template, context)


def video_hiphop_rap(request):
    video_hiphop_rap = Video.objects.all().filter(music__genre='Hip-Hop/Rap').order_by('-id')[:12]
    template = 'Music/video_hiphop_rap.html'
    context = {'video_hiphop_rap': video_hiphop_rap}
    return render(request, template, context)


def video_hiphop_pop(request):
    video_hiphop_pop = Video.objects.all().filter(Q(music__genre='Hip-Hop') | Q(music__genre='Pop')).order_by('-id')[:15]

    template = 'Music/video_hiphop_pop.html'
    context = {'video_hiphop_pop': video_hiphop_pop}
    return render(request, template, context)


def video_others(request):
    genres = ['Christian/Gospel', 'Hip-Hop/Rap', 'R&B/Soul', 'Hip-Hop', 'Pop']
    video_others = Video.objects.all().filter(~Q(music__genre__in=genres)).order_by('-id')[:12]
    template = 'Music/video_others.html'
    context = {'video_others': video_others}
    return render(request, template, context)


def song_download(request, slug):
    if request.method == 'POST':
        count = request.Get.get('count')
        add = AudioCount.objects.create(number_of_download=count)
        add.save()
    try:
        featured_artist = Audio.objects.get(slug=slug)
        artist = featured_artist.music.artist
        first_six_artist_song = Audio.objects.filter(~Q(slug=slug), music__artist=artist, publish=True).order_by('-id')[:6]
        play_audio = Audio.objects.filter(slug=slug)
    except Music.DoesNotExist:
        raise Http404("can't play or download song")
    return render(request, 'Music/song_download.html', {'play_audio': play_audio,
                                                        'first_six_artist_song': first_six_artist_song,
                                                        'featured_artist': featured_artist})


def video_download(request, slug):
    if request.method == 'POST':
        count = request.Get.get('count')
        add = VideoCount.objects.create(number_of_download=count)
        add.save()
    try:
        play_video = Video.objects.get(slug=slug)
        featured_artist = Video.objects.get(slug=slug)
        artist = featured_artist.music.artist
        first_six_artist_video = Video.objects.filter(~Q(slug=slug), music__artist=artist, publish=True).order_by('-id')[:6]
    except Video.DoesNotExist:
        raise Http404("Can't download Video")
    return render(request, 'Music/video_download.html', {'play_video': play_video,
                                                         'first_six_artist_video': first_six_artist_video,
                                                         'featured_artist': featured_artist})


def add_music(request):
    if request.method == 'POST':
        form = Addmusic(request.POST, request.FILES)
        if form.is_valid():
            song_title = request.POST.get('song_title')
            qs = Music.objects.filter(song_title=song_title)
            if qs.exists():
                messages.error(request, 'Song Title already Exist')
                form = Addmusic()
                template = 'Music/add_music.html'
                return render(request, template, {'form': form})
            else:
                music = form.save()
                messages.success(request, ' Music added successfully')
            return redirect('Music:add-audio', music_id=music.id)
    else:
        form = Addmusic()
        template = 'Music/add_music.html'
        return render(request, template, {
            'form': form
        })


def unpublished_music(request):
    unpublished = Music.objects.filter(publish=False)
    template = 'Music/unpublished_music.html'
    context = {'unpublished': unpublished}
    return render(request, template, context)


def edit_music(request, pk):
    current_user = request.user
    get_user = ProfilePic.objects.get(user=current_user)
    image = Music.objects.get(pk=int(pk))
    try:
        instance = Music.objects.get(pk=int(pk))
    except:
        instance = None

    form = Editmusic(instance=instance)
    if request.method == 'POST':
        form = Editmusic(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            music = form.save(commit=False)
            music.publish = True
            music.save()
            messages.success(request, 'Music successfully modified')
            if get_user.user_type == 'superuser':
                return redirect('Profile:superuser')
            elif get_user.user_type == 'Special_User':
                return redirect('Profile:special_user')
        # else:
        #     form = EditTalk(instance=instance)
        #     messages.error(request, "form is not valid")
        #     template = 'Talkzone/talkzone_detail.html'
        #     return render(request, template, {
        #         'form': form
        #     })

    template = 'Music/edit_music.html'
    return render(request, template, {'form': form, 'image': image})


def add_audio(request, music_id):
    music = Music.objects.get(pk=int(music_id))
    music_title = music.song_title
    current_user = request.user
    get_user = ProfilePic.objects.get(user=current_user)
    user_id = current_user.id
    if request.method == 'POST':
        check_box = request.POST.get('checks')
        form = Addaudio(request.POST, request.FILES)
        if form.is_valid():
            audio = form.save(commit=False)
            audio.music_id = int(music_id)
            audio.user_id = user_id
            get_audio = request.POST.get('audio')
            get_slug_title = request.POST.get('slug-title')
            aud = Audio.objects.filter(audio=get_audio)
            if aud.exists():
                messages.error(request, 'Audio already Exist')
                form = Addaudio()
                template = 'Music/add_audio.html'
                return render(request, template, {'form': form})
            else:
                audio.slug_title = get_slug_title
                element_to_replace = ['', '@', '&', '$', '#', "'", '"', '--', ]
                for element in element_to_replace:
                    if element in get_slug_title:
                        audio.slug = get_slug_title.replace(element, '-')
                audio.save()
                if check_box == '1':
                    messages.success(request, 'Successfully added an audio')
                    return redirect('Music:add-video', music_id=music_id)
                else:
                    messages.success(request, 'Successfully added an audio')
                    if get_user.user_type == 'superuser':
                        return redirect('Profile:superuser')
                    elif get_user.user_type == 'Special_User':
                        return redirect('Profile:special_user')
    else:
        form = Addaudio()
        context = {
            'form': form,
            'music': music,
            'music_title': music_title
        }
        return render(request, 'Music/add_audio.html', context)


def unpublished_audio(request):
    unpublished = Audio.objects.filter(publish=False)
    template = 'Music/unpublished_audio.html'
    context = {'unpublished': unpublished}
    return render(request, template, context)


def edit_audio(request, pk):
    current_user = request.user
    get_user = ProfilePic.objects.get(user=current_user)
    image = Audio.objects.get(pk=int(pk))
    try:
        instance = Audio.objects.get(pk=int(pk))
    except:
        instance = None

    form = Editaudio(instance=instance)
    if request.method == 'POST':
        form =Editaudio(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            audio = form.save(commit=False)
            audio.publish = True
            audio.save()
            messages.success(request, 'Audio successfully modified')
            if get_user.user_type == 'superuser':
                return redirect('Profile:superuser')
            elif get_user.user_type == 'Special_User':
                return redirect('Profile:special_user')


    template = 'Music/edit_audio.html'
    return render(request, template, {'form': form, 'image': image})


def add_video(request, music_id):
    current_user = request.user
    user_type = ProfilePic.objects.get(user=current_user)
    music = Music.objects.get(pk=int(music_id))
    music_title = music.song_title
    current_user = request.user
    user_id = current_user.id
    if request.method == 'POST':
        form = Addvideo(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.music_id = int(music_id)
            video.user_id = user_id
            vid = request.POST.get('video')
            get_slug_title = request.POST.get('slug-title')
            check_video = Video.objects.filter(video=vid)
            if check_video.exists():
                form = Addvideo()
                template = 'Music/add_video.html'
                return render(request, template, {'form': form})
            else:
                video.slug_title = get_slug_title

                video.slug = get_slug_title
                video.save()
                messages.success(request, 'successfully Addded new music')
                if user_type.user_type == 'superuser':
                    return redirect('Profile:superuser')
                elif user_type.user_type == 'Special_User':
                    return redirect('Profile:special_user')
                elif user_type.user_type == 'Viewers':
                    return redirect('Profile:viewers')
    else:
        form = Addvideo()
        context = {
            'form': form,
            'music': music,
            'music_title': music_title
        }
        return render(request, 'Music/add_video.html', context)


def unpublished_video(request):
    unpublished = Video.objects.filter(publish=False)
    template = 'Music/unpublished_video.html'
    context = {'unpublished': unpublished}
    return render(request, template, context)


def edit_video(request, pk):
    current_user = request.user
    user_type = ProfilePic.objects.get(user=current_user)
    image = Video.objects.get(pk=int(pk))
    try:
        instance = Video.objects.get(pk=int(pk))
    except:
        instance = None

    form = Editvideo(instance=instance)
    if request.method == 'POST':
        form =Editvideo(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            video = form.save(commit=False)
            video.publish = True
            video.save()
            messages.success(request, 'Audio successfully modified')
            if user_type.user_type == 'superuser':
                return redirect('Profile:superuser')
            elif user_type.user_type == 'Special_User':
                return redirect('Profile:special_user')
    template = 'Music/edit_video.html'
    return render(request, template, {'form': form, 'image': image})


def add_mixtape(request):
    current_user = request.user
    user_id = current_user.id
    user_type = ProfilePic.objects.get(user=current_user)
    check_box = request.POST.get('checks')
    if request.method == 'POST':
        form = AddMixtape(request.POST, request.FILES)
        if form.is_valid():
            mixtape = form.save(commit=False)
            mixtape.user_id = user_id
            tape = request.POST.get('tape_name')
            check_tape_name = Mixtape.objects.filter(tape_name=tape)
            if check_tape_name.exists():
                form = AddMixtape()
                template = 'Music/add_mixtape.html'
                return render(request, template, {'form': form})
            else:
                mixtape.slug = tape
                mixtape.save()
                if check_box == '1':
                    messages.success(request, 'Successfully added Mixtape')
                    return redirect('Music:add_mixtape')
                else:
                    messages.success(request, 'successfully Addded new Mixtape')
                    if user_type.user_type == 'superuser':
                        return redirect('Profile:superuser')
                    elif user_type.user_type == 'Special_User':
                        return redirect('Profile:special_user')
                    elif user_type.user_type == 'Viewers':
                        return redirect('Profile:viewers')
        else:
            return render(request,'Music/add_mixtape.html', {'form': form})
    else:
        form = AddMixtape()
        context = {
            'form': form,
            }
        return render(request, 'Music/add_mixtape.html', context)


def mixtape(request):
    all_tapes = Mixtape.objects.all().order_by('-id')
    paginator = Paginator(all_tapes, 20)
    page = request.GET.get('page', 1)
    try:
        tapes = paginator.page(page)
    except PageNotAnInteger:
        tapes = paginator.page(1)
    except EmptyPage:
        tapes = paginator.page(paginator.num_pages)

    template = 'Music/mixtape.html'
    context = {'tapes': tapes}
    return render(request, template, context)


def play_mixtape(request, slug):
    mixtape = Mixtape.objects.get(slug=slug)
    related_mixtape = Mixtape.objects.all().filter(~Q(slug=slug)).order_by('-id')[:6]
    template = 'Music/music_mixtape.html'
    comments = Comments.objects.filter(slug=slug)
    total = comments.count()
    print(total)
    context = {'mixtape': mixtape,
               'related_mixtape': related_mixtape,
               'comments': comments,
               'total': total
               }
    return render(request, template, context)


def save_comment(request):
    if request.method == 'POST':
        mixtape_id = int(request.POST['mixtape'])
        mixtape_slug = request.POST['mixtape_slug']
        comment = request.POST['comment']
        name = request.POST['name']
        saved_comment = Comments.objects.create(mixtape_id=mixtape_id, comment=comment, name=name, slug=mixtape_slug)
        saved_comment.save()
        # talkzone = TalkZone.objects.get(pk=talk_zone_id)
        return HttpResponseRedirect(reverse('Music:music_mixtape', kwargs={'slug': mixtape_slug}))
        # return redirect('TalkZone:talk_zone_view',)


def display_comment(request, slug):
    comment = Comments.objects.filter(slug=slug)
    total = comment.count()
    template = 'Music/music_mixtape.html'
    context = {'comment': comment, 'total': total}
    return render(request, template, context)


def unpublished_mixtape(request):
    unpublished = Mixtape.objects.filter(publish=False)
    template = 'Music/unpublished_mixtape.html'
    context = {'unpublished': unpublished}
    return render(request, template, context)


def edit_mixtape(request, pk):
    current_user = request.user
    user_id = current_user.id
    user_type = ProfilePic.objects.get(user=current_user)
    image = Mixtape.objects.get(pk=int(pk))
    try:
        instance = Mixtape.objects.get(pk=int(pk))
    except:
        instance = None

    form = EditMixtape(instance=instance)
    if request.method == 'POST':
        form = EditMixtape(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            mixtape = form.save(commit=False)
            tape = request.POST.get('tape_name')
            mixtape.user_id = user_id
            mixtape.publish = True
            mixtape.slug = tape
            mixtape.save()
            messages.success(request, 'Mixtape successfully modified')
            if user_type.user_type == 'superuser':
                return redirect('Profile:superuser')
            elif user_type.user_type == 'Special_User':
                return redirect('Profile:special_user')
        # else:
        #     form = EditTalk(instance=instance)
        #     messages.error(request, "form is not valid")
        #     template = 'Talkzone/talkzone_detail.html'
        #     return render(request, template, {
        #         'form': form
        #     })

    template = 'Music/edit_mixtape.html'
    return render(request, template, {'form': form, 'image': image})


def audiocount(request):
    if request.method == 'POST':
        count = request.POST.get('count')
        add = Audiocount.objects.create(number_of_download=count)
        add.save()




