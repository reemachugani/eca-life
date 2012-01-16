
from django import forms
from django.contrib.admin.models import User

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=True, label="First Name")
    last_name = forms.CharField(max_length=20, required=True, label="Last Name")
    email = forms.EmailField(max_length=75, label="NTU Email")
    username = forms.RegexField(regex=r'^\w+$', max_length=30,
                                error_messages={'invalid': 'This value must contain only letters, numbers, and underscores.'})
    password1 = forms.CharField(widget=forms.PasswordInput(), label="New Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Re-enter Password")

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("Username '%(username)s' is not available." % self.cleaned_data)

    def clean_email(self):
        data = self.cleaned_data.get('email', '')
        if not data or not data.endswith('ntu.edu.sg'):
             raise forms.ValidationError("You must enter your ntu.edu.sg email-id")
        else:
            try:
                user = User.objects.get(email__iexact=self.cleaned_data['email'])
            except User.DoesNotExist:
                return data
            raise forms.ValidationError("This email has already been registered!")
        return data

    def clean(self):
        if self.is_valid():
            self.cleaned_data['first_name']
            self.cleaned_data['last_name']

        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords must match.")

        return self.cleaned_data