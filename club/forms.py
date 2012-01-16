from django import forms
from club.models import Club

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        exclude = ['members','is_active']
