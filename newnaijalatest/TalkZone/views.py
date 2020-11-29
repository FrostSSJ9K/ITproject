from django.shortcuts import render, redirect
from .models import TalkZone, Comments
from django.conf import settings
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .forms import AddTalk, EditTalk
from django.contrib import messages
from Profile.models import ProfilePic
from django.views.generic.detail import DetailView


# Create your views here.
def talk_zone(request):
    talk_zone = TalkZone.objects.all().filter(publish=True).order_by('-id')[1:]
    template = 'TalkZone/talk_zone.html'
    context = {'talk_zone': talk_zone}
    return render(request, template, context)


def talk_zone_view(request, slug):
    try:
        talk_zone = TalkZone.objects.get(slug=slug)
        select_related_date = TalkZone.objects.get(slug=slug)
        related_date = select_related_date.created_on.date()
        title = select_related_date.title
        print(related_date)
        one_talk_zone = TalkZone.objects.filter(~Q(slug=slug), created_on__date=related_date, publish=True).order_by('-id')[
                          :1]
        comments = Comments.objects.filter(talk_zone=talk_zone)
        total = comments.count()
        template = 'TalkZone/talk_zone_view.html'
        ref_url = settings.SHARE_TALKZONE_URL
        context = {'talk_zone': talk_zone, 'select_related_date': select_related_date,
                   'one_talk_zone': one_talk_zone, 'title': title, 'ref_url': ref_url,
                   'comments': comments, 'total': total}
    except TalkZone.DoesNotExist:
        raise Http404("No such Post")
    return render(request, template, context)


def save_comment(request):
    if request.method == 'POST':
        talk_zone_id = int(request.POST['talk_zone'])
        slug = request.POST['slug']
        comment = request.POST['comment']
        name = request.POST['name']
        saved_comment = Comments.objects.create(talk_zone_id=talk_zone_id, comment=comment, name=name, slug=slug)
        saved_comment.save()
        # talkzone = TalkZone.objects.get(pk=talk_zone_id)
        return HttpResponseRedirect(reverse('TalkZone:talk_zone_view', kwargs={'slug': slug}))
        # return redirect('TalkZone:talk_zone_view',)


def display_comment(request, slug):
    comment = Comments.objects.filter(talk_zone=slug)
    total = comment.count()
    template = 'TalkZone/talk_zone_view.html'
    context = {'comment': comment, 'total': total}
    return render(request, template, context)


def index(request):
    posts = TalkZone.objects.all()
    return render(request, 'TalkZone/index.html', {'posts': posts})


def lazy_load_posts(request):
    page = request.POST.get('page')
    posts = TalkZone.objects.all()[:5]  # get just 5 posts

    # use Django's pagination
    # https://docs.djangoproject.com/en/dev/topics/pagination/
    results_per_page = 5
    paginator = Paginator(posts, results_per_page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(2)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # build a html posts list with the paginated posts
    posts_html = loader.render_to_string('TalkZone/posts.html', {'posts': posts})

    # package output data and return it as a JSON object
    output_data = {'posts_html': posts_html, 'has_next': posts.has_next()}
    return JsonResponse(output_data)


def add_talk(request):
    current_user = request.user
    user_id = current_user.id
    user_type = ProfilePic.objects.get(user=current_user)
    if request.method == 'POST':
        form = AddTalk(request.POST, request.FILES)
        if form.is_valid():
            talks = form.save(commit=False)
            title = request.POST.get('title')
            qs = TalkZone.objects.filter(title=title)
            if qs.exists():
                messages.error(request, 'Title already Exist')
                form = AddTalk()
                return redirect('TalkZone:add_talk', {'form': form})
            else:
                talks.user_id = user_id
                talks.publish = 'False'
                element_to_replace = ['', '@', '&', '$', '#', "'", '"', '--', ]
                for element in element_to_replace:
                    if element in title:
                        talks.slug = title.replace(element, '-')
                form.save()
                messages.success(request, ' Talk Zone successfully added')
                if user_type.user_type == 'superuser':
                    return redirect('Profile:superuser')
                elif user_type.user_type == 'Special_User':
                    return redirect('Profile:special_user')
                elif user_type.user_type == 'Viewers':
                    return redirect('Profile:viewers')
        else:
            form = AddTalk()
            messages.error(request, "form is not valid")
            template = 'TalkZone/add_talk.html'
            return render(request, template, {
                'form': form
            })
    else:
        form = AddTalk()
        template = 'TalkZone/add_talk.html'
        return render(request, template, {
            'form': form
        })


def unpublished_talkzone(request):
    all_unpublished_talkzone = TalkZone.objects.all().filter(publish=False)
    template = 'TalkZone/unpublished.html'
    context = {'all_unpublished_talkzone': all_unpublished_talkzone}
    return render(request, template, context)


def edit_talk(request, pk):
    current_user = request.user
    user_id = current_user.id
    user_profile = ProfilePic.objects.get(user=current_user)
    user_type = user_profile.user_type
    image = TalkZone.objects.filter(pk=int(pk))
    try:
        instance = TalkZone.objects.get(pk=int(pk))
    except:
        instance = None

    form = EditTalk(instance=instance)
    if request.method == 'POST':
        form = EditTalk(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            talks = form.save(commit=False)
            title = request.POST.get('title')

            #talks.user_id = user_id
            talks.publish = True
            element_to_replace = ['', '@', '&', '$', '#', "'", '"', '--', ]
            for element in element_to_replace:
                if element in title:
                    talks.slug = title.replace(element, '-')
            form.save()
            messages.success(request, 'Talk Zone successfully modified')
            if user_type == 'superuser':
                return redirect('Profile:superuser')
            elif user_type == 'Special_User':
                return redirect('Profile:special_user')

        # else:
        #     form = EditTalk(instance=instance)
        #     messages.error(request, "form is not valid")
        #     template = 'Talkzone/talkzone_detail.html'
        #     return render(request, template, {
        #         'form': form
        #     })

    template = 'TalkZone/talkzone_detail.html'
    return render(request, template, {'form': form, 'image': image})
