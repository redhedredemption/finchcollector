from django import forms
from .models import Finch, Feeding, Toy

class FinchForm(forms.ModelForm):
    class Meta:
        model = Finch
        fields = ['name', 'species', 'description', 'age']

class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),
            'meal': forms.Select(attrs={'class': 'browser-default'}),
        }

class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ['name', 'material']