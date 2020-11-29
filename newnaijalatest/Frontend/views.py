
from Music.models import Audio, Video, Mixtape
from Gist.models import GistPost
from TalkZone.models import TalkZone
from  Mysteries.models import Quote
from News.models import NewsPosts
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from datetime import datetime
from Music.models import Music
from .forms import Addconatct
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from .models import Ad_image, Ads, Contact, Ad_Provider

def base(request):
    song = Audio.objects.all().order_by('-id')[:1]
    latest_video = Video.objects.all().order_by('-id')[:1]
    time = datetime.now()
    day = time.strftime("%A")
    hour = time.hour
    if hour < 12:
        message = "Good Morning"
    elif 12 <= hour < 16:
        message = "Good afternoon"
    else:
        message = "Good Evening"

    context = {'time': time, 'message': message, 'day': day, 'song': song, 'latest_video': latest_video}
    template = 'Frontend/base.html'
    print(song)
    print(time)
    return render(request, template, context)


def search(request):
    query = request.GET.get('q')
    templates = 'Frontend/search.html'
    if Audio.objects.all().filter(Q(music__artist__iexact=query) | Q(music__artist__startswith=query) |
                                  Q(music__artist__contains=query)):

        artist_result = Audio.objects.all().filter(Q(music__artist__iexact=query) | Q(music__artist__startswith=query)
                                                   | Q(music__artist__icontains=query))
        artist_result_video = Video.objects.all().filter(Q(music__artist__iexact=query) |
                                                         Q(music__artist__startswith=query) |
                                                         Q(music__artist__contains=query))
        #artist_result_count = artist_result.count()
        context = {'artist_result': artist_result, 'get': query, 'artist_result_video': artist_result_video}

        return render(request, templates, context)
    elif Audio.objects.all().filter(Q(music__song_title__iexact=query) | Q(music__song_title__startswith=query)
                                    | Q(music__song_title__icontains=query) | Q(music__song_title__iendswith=query)):
        song_title_audio = Audio.objects.all().filter(Q(music__song_title__iexact=query) |
                                                      Q(music__song_title__startswith=query) |
                                                      Q(music__song_title__icontains=query) |
                                                      Q(music__song_title__iendswith=query))
        song_title_video = Video.objects.all().filter(Q(music__song_title__iexact=query) |
                                                      Q(music__song_title__startswith=query) |
                                                      Q(music__song_title__icontains=query)
                                                      | Q(music__song_title__iendswith=query))
        context = {'song_title_audio': song_title_audio, 'song_title_video': song_title_video}
        print(song_title_audio)
        print(song_title_video)
        return render(request, templates, context)
    #################Mixtape##################################
    elif Mixtape.objects.all().filter(Q(tape_name__iexact=query) | Q(tape_name__startswith=query)
                                      | Q(tape_name__icontains=query) | Q(tape_name__iendswith=query)):
        all_tapename = Mixtape.objects.all().filter(Q(tape_name__iexact=query) |
                                                    Q(tape_name__startswith=query) |
                                                    Q(tape_name__icontains=query) |
                                                    Q(tape_name__iendswith=query))
        context = {'all_tapename': all_tapename}
        return render(request, templates, context)
    elif Mixtape.objects.all().filter(Q(dj_name__iexact=query) | Q(dj_name__startswith=query)
                                      | Q(dj_name__icontains=query) | Q(dj_name__iendswith=query)):
        all_djname = Mixtape.objects.all().filter(Q(dj_name__iexact=query) |
                                                  Q(dj_name__startswith=query) |
                                                  Q(dj_name__icontains=query) |
                                                  Q(dj_name__iendswith=query))
        context = {'all_djname': all_djname}
        return render(request, templates, context)

    elif GistPost.objects.all().filter(Q(title__iexact=query) | Q(title__startswith=query) |
                                       Q(title__icontains=query) | Q(title__iendswith=query)):
        all_gisttitle = GistPost.objects.all().filter(Q(title__iexact=query) |
                                                      Q(title__startswith=query) |
                                                      Q(title__icontains=query) |
                                                      Q(title__iendswith=query))
        context = {'all_gisttitle': all_gisttitle}
        return render(request, templates, context)
    elif GistPost.objects.all().filter(Q(category__iexact=query) | Q(category__startswith=query) |
                                       Q(category__icontains=query) | Q(category__iendswith=query)):
        all_gistcategory = GistPost.objects.all().filter(Q(category__iexact=query) |
                                                         Q(category__startswith=query) |
                                                         Q(category__icontains=query) |
                                                         Q(category__iendswith=query))
        context = {'all_gistcategory':  all_gistcategory}
        return render(request, templates, context)
    elif GistPost.objects.all().filter(Q(poster__iexact=query) | Q(poster__startswith=query) |
                                       Q(poster__icontains=query) | Q(poster__iendswith=query)):
        all_gistposter = GistPost.objects.all().filter(Q(poster__iexact=query) |
                                                       Q(poster__startswith=query) |
                                                       Q(poster__icontains=query) |
                                                       Q(poster__iendswith=query))
        context = {'all_gistposter': all_gistposter}
        return render(request, templates, context)
    elif Quote.objects.all().filter(Q(category__iexact=query) | Q(category__startswith=query) |
                                    Q(category__icontains=query) | Q(category__iendswith=query)):
        mystery_category = Quote.objects.all().filter(Q(category__iexact=query) |
                                                         Q(category__startswith=query) |
                                                         Q(category__icontains=query) |
                                                         Q(category__iendswith=query))
        context = {'mystery_category':  mystery_category}
        return render(request, templates, context)

    elif Quote.objects.all().filter(Q(author__iexact=query) | Q(author__startswith=query) |
                                    Q(author__icontains=query) | Q(author__iendswith=query)):
        mystery_author = Quote.objects.all().filter(Q(author__iexact=query) |
                                                       Q(author__startswith=query) |
                                                       Q(author__icontains=query) |
                                                       Q(author__iendswith=query))
        context = {'mystery_author': mystery_author}
        return render(request, templates, context)

    elif TalkZone.objects.all().filter(Q(title__iexact=query) | Q(title__startswith=query) |
                                       Q(title__icontains=query) | Q(title__iendswith=query)):
        talkzone_title = TalkZone.objects.all().filter(Q(title__iexact=query) |
                                                       Q(title__startswith=query) |
                                                       Q(title__icontains=query) |
                                                       Q(title__iendswith=query))
        context = {'talkzone_title': talkzone_title}
        return render(request, templates, context)
    elif TalkZone.objects.all().filter(Q(poster__iexact=query) | Q(poster__startswith=query) |
                                       Q(poster__icontains=query) | Q(poster__iendswith=query)):
        talkzone_poster = TalkZone.objects.all().filter(Q(poster__iexact=query) |
                                                        Q(poster__startswith=query) |
                                                        Q(poster__icontains=query) |
                                                        Q(poster__iendswith=query))
        context = {'talkzone_poster': talkzone_poster}
        return render(request, templates, context)
    elif NewsPosts.objects.all().filter(Q(title__iexact=query) | Q(title__startswith=query) |
                                        Q(title__icontains=query) | Q(title__iendswith=query)):
        news_title = NewsPosts.objects.all().filter(Q(title__iexact=query) |
                                                    Q(title__startswith=query) |
                                                    Q(title__icontains=query) |
                                                    Q(title__iendswith=query))
        context = {'news_title': news_title}
        return render(request, templates, context)
    elif NewsPosts.objects.all().filter(Q(category__iexact=query) | Q(category__startswith=query) |
                                        Q(category__icontains=query) | Q(category__iendswith=query)):
        news_category = NewsPosts.objects.all().filter(Q(category__iexact=query) |
                                                       Q(category__startswith=query) |
                                                       Q(category__icontains=query) |
                                                       Q(category__iendswith=query))
        context = {'news_category': news_category}
        return render(request, templates, context)
    elif NewsPosts.objects.all().filter(Q(speaker__iexact=query) | Q(speaker__startswith=query) |
                                        Q(speaker__icontains=query) | Q(speaker__iendswith=query)):
        news_poster = NewsPosts.objects.all().filter(Q(speaker__iexact=query) |
                                                     Q(speaker__startswith=query) |
                                                     Q(speaker__icontains=query) |
                                                     Q(speaker__iendswith=query))
        context = {'news_poster': news_poster}
        return render(request, templates, context)
    else:
        messages.warning(request, "Your Search did not match")
        return redirect('Music:home1')





def add_contact(request):
    if request.method == 'POST':
        form = Addconatct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ' Music added successfully')
            return redirect('Frontend:contact-us')
    else:
        form = Addconatct()
        template = 'Frontend/contact.html'
        return render(request, template, {
            'form': form
        })

def advertisement(request):
    template = 'Frontend/advertisement.html'
    return render(request, template)


