from django import forms
from event.models import Event
from settings import DATE_INPUT_FORMATS
from django.contrib.admin import widgets

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ['club', 'date_posted', 'image', 'registered']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
#        self.fields['date'].widget = widgets.AdminDateWidget()
        self.fields['date'].initial = 'yyyy-dd-mm'
        self.fields.keyOrder = ['title','announcement', 'category','date','start_time','end_time','venue','viewership']

    def clean(self):
        
        return self.cleaned_data