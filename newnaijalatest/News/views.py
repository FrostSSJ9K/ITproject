from django.shortcuts import render, redirect
from .models import NewsPosts
from django.db.models import Q
from django.http import Http404
from .forms import AddNews, EditNews
from Profile.models import ProfilePic
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def politics(request):
    first_twelve_politics = NewsPosts.objects.all().filter(category='politics', publish=True).order_by('-id')[:12]
    last_politics = NewsPosts.objects.all().filter(category='politics', publish=True).order_by('-id')[12:]
    template = 'News/politics.html'
    context = {'first_twelve_politics': first_twelve_politics, 'last_politics': last_politics}
    return render(request,template, context)


def sport(request):
    first_tweleve_sports = NewsPosts.objects.all().filter(category='sports', publish=True).order_by('-id')[:12]
    rest_sports = NewsPosts.objects.all().filter(category='sports', publish=True).order_by('-id')[12:]
    template = 'News/sports.html'
    context = {'first_tweleve_sports': first_tweleve_sports, 'rest_sports': rest_sports}
    return render(request, template, context)


def entertainment(request):
    first_tweleve_entertainment = NewsPosts.objects.all().filter(category='entertainment', publish=True).order_by('-id')[:12]
    rest_entertainment = NewsPosts.objects.all().filter(category='entertainment', publish=True).order_by('-id')[12:]
    template = 'News/entertainment.html'
    context = {'first_tweleve_entertainment': first_tweleve_entertainment, 'rest_entertainment': rest_entertainment}
    return render(request, template, context)


def all_news(request):
    news = NewsPosts.objects.all().filter(publish=True).order_by('-id')
    paginator = Paginator(news, 36)
    page = request.GET.get('page', 1)
    try:
        newss = paginator.page(page)
    except PageNotAnInteger:
        newss = paginator.page(1)
    except EmptyPage:
        newss = paginator.page(paginator.num_pages)
    template = 'News/all_news.html'
    context = {'newss': newss}
    return render(request, template, context)


def display_news(request, slug):
    try:
        print(slug)
        news = NewsPosts.objects.filter(slug=slug)
        select_related_date = NewsPosts.objects.get(slug=slug)
        related_date = select_related_date.category
        print(related_date)
        #more_news_three = NewsPosts.objects.filter(~Q(slug=slug), created_on__date=related_date).order_by('-id')[:3]
        more_news = NewsPosts.objects.filter(~Q(slug=slug), publish=True, category=related_date).order_by('-id')[:6]
        template = 'News/display_news.html'
        context = {'news': news, 'select_related_date': select_related_date, 'more_news': more_news}
    except NewsPosts.DoesNotExist:
        raise Http404("No such Post")
    return render(request, template, context)


def add_news(request):
    current_user = request.user
    user_id = current_user.id
    user_type = ProfilePic.objects.get(user=current_user)
    if request.method == 'POST':
        form = AddNews(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            title = request.POST.get('title')
            qs = NewsPosts.objects.filter(title=title)
            if qs.exists():
                messages.error(request, 'news Title already Exist')
                form = AddNews()
                return redirect('News:addnews', {'form': form})
            else:
                news.user_id = user_id
                news.publish = False
                element_to_replace = ['', '@', '&', '$', '#', "'", '"', '--', ]
                for element in element_to_replace:
                    if element in title:

                        news.slug = title.replace(element, '-')
                form.save()
                messages.success(request, 'News added successfully')
                if user_type.user_type == 'superuser':
                    return redirect('Profile:superuser')
                elif user_type.user_type == 'Special_User':
                    return redirect('Profile:special_user')
                elif user_type.user_type == 'Viewers':
                    return redirect('Profile:viewers')
        else:
            form = AddNews()
            template = 'News/addnews.html'
            messages.warning(request, "form is invalid, check the fields")
            return render(request, template, {
                'form': form
            })
    else:
        form = AddNews()
        template = 'News/addnews.html'
        return render(request, template, {
            'form': form
        })


def unpublished_news(request):
    unpublished = NewsPosts.objects.filter(publish=False)
    template = 'News/unpublished_news.html'
    context = {'unpublished': unpublished}
    return render(request, template, context)


def edit_news(request, pk):
    current_user = request.user
    user_id = current_user.id
    user_type = ProfilePic.objects.get(user=current_user)
    image = NewsPosts.objects.filter(pk=int(pk))
    try:
        instance = NewsPosts.objects.get(pk=int(pk))
    except:
        instance = None

    form = EditNews(instance=instance)
    if request.method == 'POST':
        form = EditNews(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            news = form.save(commit=False)
            title = request.POST.get('title')

            #news.user_id = user_id
            news.publish = True
            element_to_replace = ['', '@', '&', '$', '#', "'", '"', '--', ]
            for element in element_to_replace:
                if element in title:
                    news.slug = title.replace(element, '-')
            news.save()
            messages.success(request, 'News successfully modified')
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

    template = 'News/edit_news.html'
    messages.error(request, 'something went wrong')
    return render(request, template, {'form': form, 'image': image})
