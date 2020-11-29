from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType

from Profile.models import ProfilePic
from NaijaLatest import constants


def get_content_type():
    try:
        return ContentType.objects.get_for_model(ProfilePic)
    except:
        return None


def create_default_permissions():
    ct = get_content_type()
    if not ct:
        return
    Permission.objects.get_or_create(codename='Special_User', name='Special_User', content_type=ct)
    Permission.objects.get_or_create(codename='Viewers', name='Viewers',
                                     content_type=ct)
    Permission.objects.get_or_create(codename='Temp_User', name='Temp_User', content_type=ct)


create_default_permissions()


def get_user_type(user):
    if user.is_superuser:
        return constants.SUPERUSER
    if user.has_perm("Profile.Special_User"):
        return constants.SPECIAL_USER
    if user.has_perm("Profile.Viewers"):
        return constants.VIEWERS
    if user.has_perm("Profile.Temp_User"):
        return constants.TEMP_USER
