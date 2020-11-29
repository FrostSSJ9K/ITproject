from Mysteries.models import Quote
from News.models import NewsPosts
from TalkZone.models import TalkZone
from Music.models import Mixtape, Music, Audio, Video
from Gist.models import GistPost


def unpublished(request):
    tz = TalkZone.objects.filter(publish='False')
    count = tz.count()
    quote = Quote.objects.filter(publish='False')
    count_mystery = quote.count()
    unpublished_news = NewsPosts.objects.filter(publish=False)
    count_unpublished_news = unpublished_news.count()
    mixtape = Mixtape.objects.filter(publish='False')
    count_unpublished_mixtape = mixtape.count()
    unpublished_music = Music.objects.filter(publish=False)
    count_unpublished_music = unpublished_music.count()
    audio = Audio.objects.filter(publish=False)
    count_unpublished_audio = audio.count()
    video = Video.objects.filter(publish=False)
    count_unpublished_video = video.count()
    gist = GistPost.objects.filter(publish=False)
    count_unpublished_gist = gist.count()
    total = (count_mystery + count_unpublished_news + count + count_unpublished_mixtape + count_unpublished_music
             + count_unpublished_audio + count_unpublished_video + count_unpublished_gist)

    return {
        'count_mystery': count_mystery, 'unpublished': unpublished, 'count_unpublished_news': count_unpublished_news,
        'total': total, 'count': count, 'count_unpublished_mixtape': count_unpublished_mixtape,
        'count_unpublished_music':  count_unpublished_music, 'count_unpublished_audio': count_unpublished_audio,
        'count_unpublished_video': count_unpublished_video, 'count_unpublished_gist':count_unpublished_gist# Add 'latest_song' to the context
    }
