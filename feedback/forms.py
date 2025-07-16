from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['subject', 'message', 'rating']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'message': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 4}),
            'rating': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
        }
