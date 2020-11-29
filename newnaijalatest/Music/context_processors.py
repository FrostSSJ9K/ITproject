


def song(request):
    from Music.models import Audio, Video
    from Mysteries.models import Quote
    latest_song = Audio.objects.all().filter(publish=True).order_by('-id')[:1]
    latest_video = Video.objects.all().filter(publish=True).order_by('-id')[:1]
    first_ten_mysteries = Quote.objects.all().filter(publish=True).order_by('-id')[:50]
    return {
        'song': latest_song, 'video': latest_video, 'mystery': first_ten_mysteries  # Add 'latest_song' to the context
    }