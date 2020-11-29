from django import forms
from TalkZone.models import TalkZone


class AddTalk(forms.ModelForm):
    class Meta:
        model = TalkZone
        exclude = {'slug', 'user'}
        fields = ['title',  'description', 'body', 'cover_image', 'poster']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),

            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control', 'width': '650px'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'poster': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditTalk(forms.ModelForm):
    class Meta:
        model = TalkZone
        exclude = {'slug', 'user'}
        fields = ['title',  'description', 'body', 'cover_image', 'poster']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),

            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control', 'width': '650px'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'poster': forms.TextInput(attrs={'class': 'form-control'}),
        }