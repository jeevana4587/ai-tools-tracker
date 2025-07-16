from django import forms
from .models import UserSettings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = ['theme', 'language', ]
        widgets = {
            'theme': forms.Select(attrs={'class': 'form-select'}),
            'language': forms.Select(attrs={'class': 'form-select'}),
            
        }

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

        
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']