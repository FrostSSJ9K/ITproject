from django.contrib import admin
from .models import Music, Video, Audio, Lyrics, Mixtape, Comments, AudioCount, VideoCount, MixtapeCount, dont_eat_baby_food
# Register your models here.


admin.site.register(Music)
admin.site.register(Video)
admin.site.register(Audio)
admin.site.register(Lyrics)
admin.site.register(Mixtape)
admin.site.register(Comments)
admin.site.register(AudioCount)
admin.site.register(VideoCount)
admin.site.register(MixtapeCount)
admin.site.register(dont_eat_baby_food)