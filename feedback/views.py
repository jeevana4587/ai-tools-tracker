from django.shortcuts import render
from django.shortcuts import redirect
from .forms import FeedbackForm
from .models import Feedback
from django.contrib.auth.decorators import login_required

@login_required
def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('feedback:thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/submit_feedback.html', {'form': form})

def thank_you_view(request):
    return render(request, 'feedback/thank_you.html')
