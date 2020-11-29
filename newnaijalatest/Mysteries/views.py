from django.shortcuts import render, redirect
from .models import Quote
from django.contrib import messages
from .forms import AddMysteries, EditMysteries
from Profile.models import ProfilePic
# Create your views here.


def quotes(request):
    all_quotes = Quote.objects.all().filter(category='quote', publish=True).order_by('-id')
    template = 'Mysteries/quotes.html'
    context = {'all_quotes': all_quotes}
    return render(request, template, context)


def letter(request):
    all_quotes = Quote.objects.all().filter(category='letters', publish=True).order_by('-id')
    template = 'Mysteries/letters.html'
    context = {'all_quotes': all_quotes}
    return render(request, template, context)


def poem(request):
    all_quotes = Quote.objects.all().filter(category='poem', publish=True).order_by('-id')
    template = 'Mysteries/poem.html'
    context = {'all_quotes': all_quotes}
    return render(request, template, context)


def soul_awakening(request):
    all_quotes = Quote.objects.all().filter(category='soul awakening', publish=True).order_by('-id')
    template = 'Mysteries/soul-awakening.html'
    context = {'all_quotes': all_quotes}
    return render(request, template, context)


def add_mysteries(request):
    current_user = request.user
    user_id = current_user.id
    user_type = ProfilePic.objects.get(user=current_user)
    if request.method == 'POST':
        form = AddMysteries(request.POST, request.FILES)
        if form.is_valid():
            mystery = form.save(commit=False)

            mystery.user_id = user_id

            form.save()
            messages.success(request, ' Mystery added successfully for review')
            if user_type.user_type == 'superuser':
                return redirect('Profile:superuser')
            elif user_type.user_type == 'Special_User':
                return redirect('Profile:special_user')
            elif user_type.user_type == 'Viewers':
                return redirect('Profile:viewers')
    else:
        form = AddMysteries()
        template = 'Mysteries/add_mysteries.html'
        return render(request, template, {
            'form': form
        })


def unpublished_mystery(request):
    unpublished = Quote.objects.filter(publish=False)
    template = 'Mysteries/unpublished_mystery.html'
    context = {'unpublished': unpublished}
    return render(request, template, context)


def edit_mystery(request, pk):
    current_user = request.user
    user_id = current_user.id
    user_type = ProfilePic.objects.get(user=current_user)
    image = Quote.objects.filter(pk=int(pk))
    try:
        instance =Quote.objects.get(pk=int(pk))
    except:
        instance = None

    form = EditMysteries(instance=instance)
    if request.method == 'POST':
        form = EditMysteries(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            mystery = form.save(commit=False)
           # mystery.user_id = user_id
            mystery.publish = True
            form.save()
            messages.success(request, 'Mystery successfully modified')
            if user_type.user_type == 'superuser':
                return redirect('Profile:superuser')
            elif user_type.user_type == 'Special_User':
                return redirect('Profile:special_user')
        # else:
        #     form = EditTalk(instance=instance)
        #     messages.error(request, "form is not valid")
            template = 'Mysteries/review_mysteries.html'
        #     return render(request, template, {
        #         'form': form
        #     })

    template = 'Mysteries/review_mysteries.html'
    return render(request, template, {'form': form, 'image': image})




