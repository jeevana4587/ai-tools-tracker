from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['subject', 'message', 'rating']
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors',
                'placeholder': 'Enter feedback subject...'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors',
                'rows': 5,
                'placeholder': 'Please share your feedback, suggestions, or report any issues...'
            }),
            'rating': forms.Select(attrs={
                'class': 'w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors'
            }),
        }
