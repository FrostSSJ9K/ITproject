from django.shortcuts import render, redirect
from django.http import Http404
from .forms import Addgist,Editgist
from django.contrib import messages
from .models import GistPost, MostView
from News.models import NewsPosts
from django.db.models import Q
from Profile.models import ProfilePic
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage

def gossip(request):
    first_twelve_gossip = GistPost.objects.all().filter(category='gossip', publish=True).order_by('-id')[:12]
    last_gossip = GistPost.objects.all().filter(category='gossip', publish=True).order_by('-id')[12:]
    template = 'Gist/gossip.html'
    context = {'first_twelve_gossip': first_twelve_gossip, 'last_gossip': last_gossip}
    return render(request, template, context)


def relationship(request):
    first_twelve_relationship = GistPost.objects.all().filter(category='relationship').order_by('-id')[:12]
    last_relationship = GistPost.objects.all().filter(category='relationship').order_by('-id')[:12]
    template = 'Gist/relationship.html'
    context = {'first_twelve_relationship': first_twelve_relationship, 'last_relationship':  last_relationship}
    return render(request, template, context)

def celeb(request):
    first_twelve_celeb = GistPost.objects.all().filter(category='celeb').order_by('-id')[:12]
    last_relationship = GistPost.objects.all().filter(category='celeb').order_by('-id')[12:]
    template = 'Gist/celeb.html'
    context = {'first_twelve_celeb': first_twelve_celeb, 'last_relationship': last_relationship}
    return render(request, template, context)


def wedding(request):
    first_twelve_wedding = GistPost.objects.all().filter(category='wedding').order_by('-id')[:12]
    last_wedding = GistPost.objects.all().filter(category='wedding').order_by('-id')[12:]
    template = 'Gist/wedding.html'
    context = {'first_twelve_wedding': first_twelve_wedding, 'last_wedding': last_wedding}
    return render(request, template, context)


def all_gist(request):
    gist = GistPost.objects.all().filter(publish=True).order_by('-id')
    paginator = Paginator(gist, 20)
    page = request.GET.get('page', 1)
    try:
        gists = paginator.page(page)
    except PageNotAnInteger:
        gists = paginator.page(1)
    except EmptyPage:
        gists = paginator.page(paginator.num_pages)

    template = 'Gist/all_gist.html'
    context = {'gists': gists}
    return render(request, template, context)


def display_gist(request, slug):
    try:
        gist = GistPost.objects.get(slug=slug)
        select_related_date = GistPost.objects.get(slug=slug)
        related_date = select_related_date.category
        title = select_related_date.title
        print(related_date)
        #more_gist_three = GistPost.objects.filter(~Q(slug=slug), category=related_date).order_by('-id')[:3]

        more_gist = GistPost.objects.filter(~Q(slug=slug), category=related_date).order_by('-id')[:6]
        template = 'Gist/display_gist.html'
        ref_url = settings.SHARE_URL
        context = {'gist': gist, 'select_related_date': select_related_date, 'more_gist': more_gist,
                    'title': title, 'ref_url': ref_url}
    except NewsPosts.DoesNotExist:
        raise Http404("No such Post")
    return render(request, template, context)


def share_gist(request, gist_id):
    share = GistPost.objects.get(pk=int(gist_id))
    gist = share.title
    ref_url = settings.SHARE_URL + str(gist)
    template = 'Gist/share_gist.html'
    context = {'share': share, 'ref_url': ref_url}
    return render(request, template, context)



def saveviewd(request, gist_id):
    if request.method == 'POST':
        get_id = GistPost.objects.get(pk=int(gist_id))
        owner = get_id.pk
        create_view = MostView.objects.create(what_viewd_id=owner)
        create_view.save()


def add_gist(request):
    current_user = request.user
    user_id = current_user.id
    user_type = ProfilePic.objects.get(user=current_user)
    if request.method == 'POST':
        form = Addgist(request.POST, request.FILES)
        if form.is_valid():
            gist = form.save(commit=False)
            title = request.POST.get('title')
            qs = GistPost.objects.filter(title=title)
            if qs.exists():
                messages.error(request, 'Song Title already Exist')
                form = Addgist()
                return redirect('Gist:add-gist', {'form': form})
            else:
                gist.user_id = user_id
                element_to_replace = ['', '@', '&', '$', '#', "'", '"', '--', ]
                for element in element_to_replace:
                    if element in title:

                        gist.slug = title.replace(element, '-')
                form.save()
                messages.success(request, ' Music added successfully')
                if user_type.user_type == 'superuser':
                    return redirect('Profile:superuser')
                elif user_type.user_type == 'Special_User':
                    return redirect('Profile:special_user')
                elif user_type.user_type == 'Viewers':
                    return redirect('Profile:viewers')
        else:
            form = Addgist()
            template = 'Gist/add-gist.html'
            messages.warning(request, "Check all the field very well")
            return render(request, template, {
                'form': form
            })
    else:
        form = Addgist()
        template = 'Gist/add-gist.html'
        return render(request, template, {
            'form': form
        })


def unpublished_guest(request):
    unpublished = GistPost.objects.filter(publish=False)
    template = 'Gist/unpublished_gist.html'
    context = {'unpublished': unpublished}
    return render(request, template, context)


def edit_gist(request, pk):
    current_user = request.user
    user_id = current_user.id
    user_type = ProfilePic.objects.get(user=current_user)
    image = GistPost.objects.get(pk=int(pk))
    try:
        instance = GistPost.objects.get(pk=int(pk))
    except:
        instance = None

    form = Editgist(instance=instance)
    if request.method == 'POST':
        form = Editgist(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            gist = form.save(commit=False)
            #gist.user_id = user_id
            gist.publish = True
            #gist.publish = True
            gist.save()
            messages.success(request, 'Gist successfully modified')
            if user_type.user_type == 'superuser':
                return redirect('Profile:superuser')
            elif user_type.user_type == 'Special_User':
                return redirect('Profile:special_user')
    template = 'Gist/edit_gist.html'
    return render(request, template, {'form': form, 'image': image})
