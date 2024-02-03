from .models import articls
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea,ImageField,ClearableFileInput

class articlsform(ModelForm):
    class Meta:
        model = articls
        fields = ['title', 'anons', 'haracter', 'date','image']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            "haracter": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Характеристики'
            }),
            "image": ClearableFileInput(attrs={'class': 'form-control'}),
        
        }
