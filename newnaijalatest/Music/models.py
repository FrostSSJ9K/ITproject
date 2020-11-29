from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from  ckeditor.fields import RichTextField, CKEditorWidget
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin
# Create your models here.


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.username, filename)


class Music(models.Model):
    song_title = models.CharField(max_length=500)
    album = models.CharField(default='No Album', max_length=500)
    genre = models.CharField(max_length=500)
    released_Year = models.CharField(max_length=200, blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to='cover_imgae/', blank=True)
    uploader = models.CharField(max_length=200)
    artist = models.CharField(default='None', max_length=200)
    featured_artist = models.CharField(default='None', max_length=200)
    about_song = RichTextField(max_length=3000, config_name='special')
    publish = models.BooleanField(default=False)

    # create a string representation of song
    def __str__(self):
        return self.song_title


class Video(models.Model,  HitCountMixin):
    video = models.FileField(upload_to=user_directory_path, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='videos', on_delete=models.DO_NOTHING)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=500, unique=True, null=True)
    slug_title = models.CharField(max_length=500, null=True)
    youtube_link = RichTextUploadingField(default="add youtube link here", config_name='default',
                                         external_plugin_resources=[('Youtube',
                                                                      '/NaijaLatest/static/ckeditor/ckeditor/plugins/youtube/',
                                                                      'plugin.js',)],
                                          )
    publish = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')
    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug_title)
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.video)



class VideoCount(models.Model):
    number_of_download =models.ForeignKey(Video, on_delete=models.DO_NOTHING)


class Audio(models.Model):
    audio = models.FileField(upload_to=user_directory_path, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='audios', on_delete=models.DO_NOTHING)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to=user_directory_path, blank=True)
    slug = models.SlugField(max_length=500, unique=True, null=True)
    slug_title = models.CharField(max_length=500, null=True)
    publish = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug_title)
        super(Audio, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.audio)


class AudioCount(models.Model):
    number_of_download = models.ForeignKey(Audio, on_delete=models.DO_NOTHING)

class UserPlayVideo(models.Model):
    user = models.ForeignKey(User,related_name='playvideo', on_delete=models.DO_NOTHING)
    video = models.ForeignKey(Video, on_delete=models.DO_NOTHING)


class UserDownloadVideo(models.Model):
    user = models.ForeignKey(User,related_name='downloadvideo', on_delete=models.DO_NOTHING)
    video = models.ForeignKey(Video, on_delete=models.DO_NOTHING)


class UserPlayAudio(models.Model):
    user = models.ForeignKey(User, related_name='playaudio', on_delete=models.DO_NOTHING)
    audio = models.ForeignKey(Audio, on_delete=models.DO_NOTHING)


class UserDownloadAudio(models.Model):
    user = models.ForeignKey(User, related_name='downloadaudio', on_delete=models.DO_NOTHING)
    audio = models.ForeignKey(Audio, on_delete=models.DO_NOTHING)


class Lyrics(models.Model):
    lyric = models.TextField()
    music = models.ForeignKey(Music, on_delete=models.DO_NOTHING)


class Confirmemail(models.Model):
    confirm_email = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Mixtape(models.Model):
    tape_name = RichTextField(max_length=1000, config_name='special')
    slug = models.SlugField(max_length=1000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mixtape', on_delete=models.DO_NOTHING)
    tape = models.FileField(upload_to=user_directory_path, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tracks = RichTextUploadingField(max_length=5000, default="add youtube link here", config_name='default',
                                    external_plugin_resources=[('Youtube', '/NaijaLatest/static/ckeditor/ckeditor/plugins/youtube/',

                                                               'plugin.js',)],
                                    )
    dj_description = RichTextUploadingField(config_name='special')
    tape_image = models.FileField(upload_to=user_directory_path, blank=True)
    publish = models.BooleanField(default=False)
    dj_name = models.CharField(default='Dj Appostle', max_length=200
                               )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.tape_name)
        super(Mixtape, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.tape_name)


class MixtapeCount(models.Model):
    number_of_download = models.ForeignKey(Mixtape, on_delete=models.DO_NOTHING)


#class Videos(models.Model):
    #music = models.ForeignKey(Music,on_delete=models.CASCADE)
    #video = models.FileField(upload_to='videos/', null=True, verbose_name="")
    #cover_image = models.ImageField(upload_to= 'video_image')

    #def __str__(self):
        #return str(self.video)

#class Audios(models.Model):
    #music = models.ForeignKey(Music,on_delete=models.CASCADE)
    #audio = models.FileField(upload_to='audio', blank=True, verbose_name="")
    #cover_image = models.ImageField(upload_to='audio_image')

    #def __str__(self):
        #return str(self.audio)

class Comments(models.Model):
    mixtape = models.ForeignKey(Mixtape, on_delete=models.DO_NOTHING)
    comment = models.TextField()
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class dont_eat_baby_food(models.Model):
    Name = models.CharField(max_length=200,)
    Temp = models.CharField(max_length=200,)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')



