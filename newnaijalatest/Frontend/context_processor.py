from datetime import datetime
from TalkZone.models import TalkZone

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
            'time': time, 'day': day, 'message': message  # Add 'latest_song' to the context
        }


def talkzone(request):
    slide_title = TalkZone.objects.all().filter(publish=True).order_by('-id')
    return {
        'slide_title': slide_title
    }
