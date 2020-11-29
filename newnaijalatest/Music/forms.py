from django import forms
from Music.models import Music,Audio,Video, Mixtape


class Addmusic(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['song_title', 'album', 'genre', 'released_Year', 'cover_image', 'uploader', 'artist',
                  'featured_artist', 'about_song']
        widgets = {
            'song_title': forms.TextInput(attrs={'class': 'form-control'}),
            'album': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'released_Year': forms.TextInput(attrs={'class': 'form-control'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'uploader': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'artist': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_artist': forms.TextInput(attrs={'class': 'form-control'}),
            'about_song': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Editmusic(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['song_title', 'album', 'genre', 'released_Year', 'cover_image', 'uploader', 'artist',
                  'featured_artist', 'about_song']
        widgets = {
            'song_title': forms.TextInput(attrs={'class': 'form-control'}),
            'album': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'released_Year': forms.TextInput(attrs={'class': 'form-control'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'uploader': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'artist': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_artist': forms.TextInput(attrs={'class': 'form-control'}),
            'about_song': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Addaudio(forms.ModelForm):
    class Meta:
        model = Audio
        exclude = {'music', 'user', 'slug', 'slug_title'}

        fields = ['audio', 'cover_image']

        widgets = {'audio': forms.FileInput(attrs={'class': 'form-control'}),

                   'cover_image': forms.FileInput(attrs={'class': 'form-control'}),

                   }


class Editaudio(forms.ModelForm):
    class Meta:
        model = Audio
        exclude = {'music', 'user', 'slug', 'slug_title'}

        fields = ['audio', 'cover_image']

        widgets = {'audio': forms.FileInput(attrs={'class': 'form-control'}),

                   'cover_image': forms.FileInput(attrs={'class': 'form-control'}),

                   }


class Addvideo(forms.ModelForm):
    class Meta:
        model = Video
        exclude = {'music', 'user', 'slug', 'slug_title'}
        fields = {'video', 'youtube_link'}

        widgets = {'audio': forms.FileInput(attrs={'class': 'form-control'}),
                   'youtube_link': forms.TextInput(attrs={'class': 'form-control'}),

                   }


class Editvideo(forms.ModelForm):
    class Meta:
        model = Video
        exclude = {'music', 'user', 'slug', 'slug_title'}
        fields = {'video'}

        widgets = {'audio': forms.FileInput(attrs={'class': 'form-control'}),
                   }



class AddMixtape(forms.ModelForm):
    class Meta:
        model = Mixtape
        exclude = {'user', 'slug'}
        fields = {'tape_name', 'tape', 'tracks', 'dj_description', 'tape_image'}

        widgets = {'tape_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'tape': forms.FileInput(attrs={'class': 'form-control'}),
                   'tracks': forms.TextInput(attrs={'class': 'form-control'}),
                   'dj_description': forms.TextInput(attrs={'class': 'form-control'}),
                   'tape_image': forms.FileInput(attrs={'class': 'form-control'}),
                   }


class EditMixtape(forms.ModelForm):
    class Meta:
        model = Mixtape
        exclude = {'user', 'slug'}
        fields = {'tape_name', 'tape', 'tracks', 'dj_description', 'tape_image'}

        widgets = {'tape_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'tape': forms.FileInput(attrs={'class': 'form-control'}),
                   'tracks': forms.TextInput(attrs={'class': 'form-control'}),
                   'dj_description': forms.TextInput(attrs={'class': 'form-control'}),
                   'tape_image': forms.FileInput(attrs={'class': 'form-control'}),
                   }
