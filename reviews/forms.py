from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)]

    stars = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Review
        fields = ['stars', 'review']
        widgets = {
            'review': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3}),
        }
