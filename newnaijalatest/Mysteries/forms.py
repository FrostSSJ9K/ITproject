from django import forms
from Mysteries.models import Quote


class AddMysteries(forms.ModelForm):
    class Meta:
        model = Quote
        exclude = {'user'}
        fields = ['message', 'quote_picture', 'category', 'author']
        widgets = {
            'message': forms.TextInput(attrs={'class': 'form-control'}),
            'quote_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditMysteries(forms.ModelForm):
    class Meta:
        model = Quote
        exclude = {'user'}
        fields = ['message', 'quote_picture', 'category', 'author']
        widgets = {
            'message': forms.TextInput(attrs={'class': 'form-control'}),
            'quote_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }