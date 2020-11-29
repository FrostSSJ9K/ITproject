from django import template
from django.contrib.auth.models import Group
from datetime import datetime
register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
    except Group.DoesNotExist:
        return False

    return group in user.groups.all()


def times(request):
    time = datetime.now()
    day = time.strftime("%A")
    hour = time.hour
    if hour < 12:
        message = "Good Morning"
    elif 12 <= hour < 16:
        message = "Good afternoon"
    else:
        message = "Good Evening"
    return {
        'time': time, 'day': day, 'message': message
    }