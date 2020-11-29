from TalkZone.models import TalkZone


def unpublished(request):
    unpublished = TalkZone.objects.filter(publish='False')
    counte = unpublished.count()

    return {
        'counte': counte, 'unpublished': unpublished  # Add 'latest_song' to the context
    }
