from django import forms
from .models import Review, ReviewReport

class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)]

    stars = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500'
        }),
        label="Rating"
    )

    class Meta:
        model = Review
        fields = ['stars', 'title', 'comment', 'pros', 'cons']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'placeholder': 'Brief title for your review (optional)'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-textarea mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'rows': 4,
                'placeholder': 'Share your overall experience with this tool...'
            }),
            'pros': forms.Textarea(attrs={
                'class': 'form-textarea mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'rows': 3,
                'placeholder': 'What did you like about this tool? (optional)'
            }),
            'cons': forms.Textarea(attrs={
                'class': 'form-textarea mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'rows': 3,
                'placeholder': 'What could be improved? (optional)'
            }),
        }
        labels = {
            'title': 'Review Title',
            'comment': 'Your Review',
            'pros': 'What You Liked',
            'cons': 'Areas for Improvement',
        }

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if comment and len(comment.strip()) < 10:
            raise forms.ValidationError("Please provide a more detailed review (at least 10 characters).")
        return comment

class ReviewReportForm(forms.ModelForm):
    class Meta:
        model = ReviewReport
        fields = ['reason', 'description']
        widgets = {
            'reason': forms.Select(attrs={
                'class': 'form-select rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'rows': 3,
                'placeholder': 'Please provide additional details about why you are reporting this review...'
            }),
        }
        labels = {
            'reason': 'Report Reason',
            'description': 'Additional Details (optional)',
        }

class ReviewFilterForm(forms.Form):
    SORT_CHOICES = [
        ('newest', 'Newest First'),
        ('oldest', 'Oldest First'),
        ('highest_rated', 'Highest Rated'),
        ('lowest_rated', 'Lowest Rated'),
        ('most_helpful', 'Most Helpful'),
    ]
    
    RATING_FILTER_CHOICES = [
        ('all', 'All Ratings'),
        ('5', '5 Stars'),
        ('4', '4 Stars'),
        ('3', '3 Stars'),
        ('2', '2 Stars'),
        ('1', '1 Star'),
    ]
    
    sort_by = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select rounded-md border-gray-300 shadow-sm'
        })
    )
    
    rating_filter = forms.ChoiceField(
        choices=RATING_FILTER_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select rounded-md border-gray-300 shadow-sm'
        })
    )
    
    verified_only = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-checkbox rounded border-gray-300 text-blue-600 focus:ring-blue-500'
        }),
        label='Verified reviews only'
    )
