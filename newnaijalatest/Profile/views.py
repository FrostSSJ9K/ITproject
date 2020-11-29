from django.shortcuts import render, redirect
from .forms import ProfilePic
from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime
from django.db.models import Q
from django.utils.http import urlsafe_base64_encode
from django.http import HttpResponse
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_decode
from Music.models import Music, Video, Audio,Confirmemail,Mixtape, Lyrics
from Gist.models import GistPost
from TalkZone.models import TalkZone
from Mysteries.models import Quote
from News.models import NewsPosts
from django.contrib.auth.decorators import login_required
from  Music.token import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate, login as auth_login,logout
from django.template.loader import render_to_string
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import ProfilePic
from Profile.permissions import get_content_type
from django.urls.base import reverse
import json


@login_required
def choose_profile(request):
    user = request.user
    if user.is_superuser:
        return redirect(reverse('Profile:superuser'))
    elif user.has_perm('Profile.Special_User'):
        return redirect(reverse('Profile:special_user'))
    elif user.has_perm('Profile.Viewers'):
        return redirect(reverse('Profile:viewers'))
    elif user.has_perm('Profile.Temp_User'):
        return redirect(reverse('Music:home1'))


def superuser(request):
    template = 'Profile/superuser_dashboard.html'
    current_user = request.user
    user_id = current_user.id
    user_uploaded_song = Audio.objects.all().filter(user_id=user_id)
    user_uploaded_video = Video.objects.all().filter(user_id=user_id)
    user_uploaded_gist = GistPost.objects.all().filter(user_id=user_id)
    user_uploaded_news = NewsPosts.objects.all().filter(user_id=user_id)
    user_uploaded_talk = TalkZone.objects.all().filter(user_id=user_id)
    user_uploaded_mixtape = Mixtape.objects.all().filter(user_id=user_id)
    user_uploaded_mystery = Quote.objects.all().filter(user_id=user_id)

    context = {'user_uploaded_song': user_uploaded_song, 'user_uploaded_video': user_uploaded_video,
               'user_uploaded_gist': user_uploaded_gist, 'user_uploaded_news': user_uploaded_news,
               'user_uploaded_talk': user_uploaded_talk,'user_uploaded_mystery': user_uploaded_mystery,
               'user_uploaded_mixtape': user_uploaded_mixtape}
    return render(request, template,context)


@login_required(login_url='/Profile/login')
def special_user(request):
    template = 'Profile/special_user_dashboard.html'
    current_user = request.user
    user_id = current_user.id
    user_uploaded_song = Audio.objects.all().filter(user_id=user_id)
    user_uploaded_video = Video.objects.all().filter(user_id=user_id)
    user_uploaded_gist = GistPost.objects.all().filter(user_id=user_id)
    user_uploaded_news = NewsPosts.objects.all().filter(user_id=user_id)
    user_uploaded_talk = TalkZone.objects.all().filter(user_id=user_id)
    user_uploaded_mixtape = Mixtape.objects.all().filter(user_id=user_id)
    user_uploaded_mystery = Quote.objects.all().filter(user_id=user_id)
    context = {'user_uploaded_song': user_uploaded_song, 'user_uploaded_video': user_uploaded_video,
               'user_uploaded_gist': user_uploaded_gist, 'user_uploaded_news': user_uploaded_news,
               'user_uploaded_talk': user_uploaded_talk, 'user_uploaded_mystery': user_uploaded_mystery,
               'user_uploaded_mixtape': user_uploaded_mixtape}
    return render(request, template, context)


@login_required(login_url='/Profile/login')
def viewers(request):
    template = 'Profile/viewers_dashboard.html'
    current_user = request.user
    user_id = current_user.id
    user_uploaded_song = Audio.objects.all().filter(user_id=user_id)
    user_uploaded_video = Video.objects.all().filter(user_id=user_id)
    user_uploaded_gist = GistPost.objects.all().filter(user_id=user_id)
    user_uploaded_news = NewsPosts.objects.all().filter(user_id=user_id)
    user_uploaded_talk = TalkZone.objects.all().filter(user_id=user_id)
    user_uploaded_mixtape = Mixtape.objects.all().filter(user_id=user_id)
    user_uploaded_mystery = Quote.objects.all().filter(user_id=user_id)
    context = {'user_uploaded_song': user_uploaded_song, 'user_uploaded_video': user_uploaded_video,
               'user_uploaded_gist': user_uploaded_gist, 'user_uploaded_news': user_uploaded_news,
               'user_uploaded_talk': user_uploaded_talk, 'user_uploaded_mystery': user_uploaded_mystery,
               'user_uploaded_mixtape': user_uploaded_mixtape}
    return render(request, template, context)


def dashboard(request):
    current_user = request.user
    user_id = current_user.id
    profile_pic = ProfilePic.objects.filter(user_id=user_id)
    context = {'profile_pic': profile_pic}
    template = 'Profile/base.html'
    return render(request, template, context)


def profile(request):
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Profile:login')
    else:
        form = ProfilePic(request.POST, request.FILES)
    return render(request, 'Profile/profil.html', {'form': form})


def sign_up_with_confirmation_mail(request):

    if request.method == 'POST':
        firstname = request.POST['first_name']
        firstname1 = firstname.lower()
        lastname = request.POST['last_name']
        lastname1 = lastname.lower()
        email = request.POST['email']
        email1 = email.lower()
        username = request.POST['username']
        username1 = username.lower()
        password = request.POST['password']
        #password1 = password.lower()
        picture = request.POST['picture']

        check_user_exist = User.objects.filter(Q(username=username1) | Q(email=email1)) .exists()
        if check_user_exist:
            messages.success(request, 'User already exist.')
            return redirect('Music:home1')
        else:
            user = User.objects.create_user(first_name=firstname1, last_name=lastname1, email=email1,
                                                   username=username1, password=password, is_active=False)
            user.save()
            creat_profile = ProfilePic.objects.create(user_id=user.id, picture=picture)
            creat_profile.save()

            assign_user_permission(user)
            current_site = get_current_site(request)
            message = render_to_string('Profile/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            subject = 'Activate Your NaijaLatest Account'
            to_email = email
            email = EmailMessage(subject, message, to=[to_email])
            email.send()
            return redirect('Profile:account_activation_sent')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        print('+++++++')
        print(uid)
        print('+++++++')
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        print('Nothing is showing')
        print('-------------------------')
        print(uidb64)
        print('-------------------------')
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Registration successful')
        #auth_login(request, user)
        return redirect('Profile:login')
    else:
        return render(request, 'Profile/account_activation_invalid.html')


def account_activation_sent(request):

    return render(request, 'Profile/account_activation_sent.html')


def account_activation_invalid(request):
    return render(request, 'Profile/account_activation_invalid.html')


def login(request):
    template = 'Profile/login.html'
    return render(request, template)


def loginn(request):
    if request.method == 'POST':
        email = request.POST['email']
        lower = email.lower()
        password = request.POST['password']
        print(email)
        user = authenticate(username=lower, password=password)
        if user is not None:
            if user.is_active:
                # log user in
                auth_login(request, user)
                return redirect('Profile:choose_profile')
        else:
            messages.warning(request, 'username or password does not match')
            return redirect('Music:home1')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Kindly click on Login link on the Footer to Login')
        return redirect('Music:home1')



#@login_required(login_url='/Profile/login')
'''def user_dashboard(request):
    current_user = request.user
    user_id = current_user.id
    user_uploaded_song = Audio.objects.all().filter(user_id=user_id)
    user_uploaded_video = Video.objects.all().filter(user_id=user_id)
    user_uploaded_gist = GistPost.objects.all().filter(user_id=user_id)
    user_uploaded_news = NewsPosts.objects.all().filter(user_id=user_id)
    user_uploaded_talk = TalkZone.objects.all().filter(user_id=user_id)

    context = {'user_uploaded_song': user_uploaded_song, 'user_uploaded_video': user_uploaded_video,
               'user_uploaded_gist': user_uploaded_gist, 'user_uploaded_news': user_uploaded_news,
               'user_uploaded_talk': user_uploaded_talk}
    return render(request, context)'''


def text(request):
    template = 'Profile/test.html'
    return render(request, template)


def search_status(request):

    if request.method == "GET":
        search_text = request.GET['search_text']
        if search_text is not None and search_text != u"":
            search_text = request.GET['search_text']
            statuss = Music.objects.filter(artist__contains = search_text)
        else:
            statuss = []

        return render(request, 'Profile/ajax_search.html', {'statuss':statuss})


def autocomplete(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = Music.objects.filter(artist__startswith=q)
        results = []
        print(q)

        for r in search_qs:
            results.append(r.song_title)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def password_forgot(request):
    template = 'Profile/password_reset_form.html'
    return render(request, template)


def password_reset(request):

    if request.method == 'POST':
        email = request.POST['email']
        get_user_email = User.objects.filter(email=email).exists()
        if get_user_email:
            user_email = User.objects.get(email=email)
            user = user_email.username
            mail = user_email.email
            current_site = get_current_site(request)
            message = render_to_string('Profile/activate_password.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user_email.pk)).decode(),
                'token': account_activation_token.make_token(user_email),
            })
            subject = 'Reset Your Password'
            to_email = mail
            email = EmailMessage(subject, message, to=[to_email])
            email.send()
            return redirect('Profile:password_reset_email')

        else:
            messages.warning(request, 'Email does not exist')
            return redirect('Profile:password_reset_form')


def password_reset_email(request):

    return render(request, 'Profile/password_reset_email.html')


def change_password(request, uidb64, token):
    if request.method == 'POST':
        uid = urlsafe_base64_decode(uidb64).decode()
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            get_user_password = User.objects.get(pk=uid)
            get_user_password.set_password(password)
            get_user_password.save()
            messages.success(request, 'password changed successfull. click on the login blow')
            return redirect('Music:home1')

    return render(request, 'Profile/change_password.html')


#@login_required(login_url='/Profile/login')
def assign_user_permission(user):
    ct = get_content_type()
    if not ct:
        return
    a = User.objects.get(pk=user.id)
    user_info = ProfilePic.objects.get(user=a)
    if user_info.user_type == 'Special_User':
        user.has_perm('Profile.Special_User')
        permission = Permission.objects.get(
            codename='Special_User',
            content_type=ct
        )
        user.user_permissions.add(permission)
    elif user_info.user_type == 'Viewers':
        user.has_perm('Profile.Viewers')
        permission = Permission.objects.get(
            codename='Viewers',
            content_type=ct
        )
        user.user_permissions.add(permission)
    elif user_info.user_type == 'Temp_User':
        user.has_perm('Profile.Temp_User')
        permission = Permission.objects.get(
            codename='Temp_User',
            content_type=ct
        )
        user.user_permissions.add(permission)
    user.save()


@login_required(login_url='/Profile/login')
def change_user_permission(user):
    ct = get_content_type()
    if not ct:
        return
    a = User.objects.get(username=user.user)
    user_info = ProfilePic.objects.get(user=a)
    if user_info.user_type == 'Special_User':
        a.user_permissions.clear()
        a.has_perm('Profile.Special_User')
        permission = Permission.objects.get(
            codename='Special_User',
            content_type=ct
        )
        a.user_permissions.add(permission)
    elif user_info.user_type == 'Viewers':
        a.user_permissions.clear()
        a.has_perm('Profile.Viewers')
        permission = Permission.objects.get(
            codename='Viewers',
            content_type=ct
        )
        a.user_permissions.add(permission)
    elif user_info.user_type == 'Temp_User':
        a.user_permissions.clear()
        a.has_perm('Profile.Temp_User')
        permission = Permission.objects.get(
            codename='Temp_User',
            content_type=ct
        )
        a.user_permissions.add(permission)
    a.save()


def permission(request):
    group = Group.objects.all()
    user = User.objects.all()
    viewer = User.objects.filter(groups__name='Viewers')
    staff = User.objects.filter(groups__name='Special_Users')
    template = 'Profile/permission.html'
    context = {'group': group, 'user': user, 'viewer': viewer, 'staff': staff}
    return render(request, template, context)


@login_required(login_url='/Profile/login')
def display_user_type(request):
    users_in_special = ProfilePic.objects.filter(user_type='Special_User')
    users_in_viewers = ProfilePic.objects.filter(user_type='Viewers')
    users_in_tempuser = ProfilePic.objects.filter(user_type='Temp_User')
    user_type = ProfilePic.objects.all().filter(~Q(user_type='superuser'))
    user = User.objects.all()
    print(users_in_special)
    template = 'Profile/access.html'
    context = {'users_in_special': users_in_special, 'users_in_viewers': users_in_viewers,
               'users_in_tempuser': users_in_tempuser, 'user_type': user_type, 'user': user}
    return render(request, template, context)


def change_user_type(request):
    if request.method == 'POST':
        user_id = request.POST['users']
        print(user_id)
        user_type = request.POST['user_type']
        user = User.objects.get(pk=int(user_id))
        check = ProfilePic.objects.get(user_id=user)
        if user_type == '':
            messages.warning(request, 'No radio checked')
            return redirect('Profile:access')
        else:
            if check.user_type == user_type:
                messages.warning(request, 'User already exist')
                return redirect('Profile:access')
            else:
                check.user_type = user_type
                check.save()
                print(user)
                change_user_permission(check)
                return redirect('Profile:access')


def add_user(request):
    if request.method == 'POST':
        user_id = request.POST['users']
        grp = request.POST['Special_Users']
        user = User.objects.get(pk=user_id)
        if grp == "":
            messages.warning(request,'Please select Group')
            return redirect('Profile:permission')
        else:
            if grp == 'Special_Users':
                if user.groups.filter(name='Special_Users').exists():
                    messages.warning(request, 'User already exist')
                    return redirect('Profile:permission')
                else:
                    Add_user = Group.objects.get(name='Special_Users')

                    user.groups.add(Add_user)
                    if user.groups.filter(name='Viewers').exists():
                        remove_user = Group.objects.get(name='Viewers')
                        remove_user.user_set.remove(user)
                        messages.success(request, 'User successfully Added')
                    return redirect('Profile:permission')
            elif grp =='Viewers':
                if user.groups.filter(name='Viewers').exists():
                    messages.warning(request, 'User already exist')
                    return redirect('Profile:permission')
                else:
                    Add_user = Group.objects.get(name='Viewers')
                    user.groups.add(Add_user)
                    if user.groups.filter(name='Viewers').exists():
                        remove_user = Group.objects.get(name='Special_Users')
                        remove_user.user_set.remove(user)
                        messages.success(request, 'User successfully Added')
                    return redirect('Profile:permission')


def delete_user(request):
    if request.method == 'POST':
        user_id = request.POST['deleteuser']
        grp = request.POST['Special_Users']

        user = User.objects.get(pk=user_id)
        if grp == 'Special_Users':
            if user.groups.filter(name='Special_Users').exists():
                deleteuser = Group.objects.get(name=grp)
                deleteuser.user_set.remove(user)
                messages.success(request, 'User successfully Removed')
                return redirect('Profile:permission')
            else:
                messages.warning(request, 'No such user in group')
                return redirect('Profile:permission')
        elif grp == 'Viewers':
            if user.groups.filter(name='Viewers').exists():
                deleteuser = Group.objects.get(name=grp)
                deleteuser.user_set.remove(user)
                messages.success(request, 'User successfully Removed')
                return redirect('Profile:permission')
            else:
                messages.warning(request, 'No such user in group')
                return redirect('Profile:permission')


def edit_user_profile(request):
    current_user = request.user
    user_id = current_user.id
    user_detail = ProfilePic.objects.get(user=user_id)
    template = 'Profile/edit_user_profile.html'
    context = {'user_detail': user_detail}
    return render(request, template, context)


def save_user_edit(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['USERNAME']
        picture = request.POST['picture']
        user = ProfilePic.objects.get(pk=int(userid))
        main = User.objects.get(pk=int(userid))
        if picture == "":
            user.pk = int(userid)
            user.save()
            main.first_name = firstname
            main.last_name = lastname
            main.email = email
            main.username = username
            main.save()
            messages.success(request, 'profile edited successfully')
            if user.user_type == 'Special_User':
                return redirect('Profile:special_user')
            elif user.user_type == 'superuser':
                return redirect('Profile:superuser')
            else:
                return redirect('Profile:viewers')
        else:
            user.pk = int(userid)
            user.picture = picture
            user.save()
            main.first_name = firstname
            main.last_name = lastname
            main.email = email
            main.username = username
            main.save()
            messages.success(request, 'profile edited successfully')
            if user.user_type == 'Special_User':
                return redirect('Profile:special_user')
            elif user.user_type == 'superuser':
                return redirect('Profile:superuser')
            else:
                return redirect('Profile:viewers')
