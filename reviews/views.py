from django.shortcuts import render, get_object_or_404, redirect
from tools.models import Tool
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def add_review(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)
    try:
        review = Review.objects.get(user=request.user, tool=tool)
    except Review.DoesNotExist:
        review = None

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.tool = tool
            review.stars = int(form.cleaned_data['stars'])
            review.save()
            messages.success(request, "Your review has been submitted successfully.")
            return redirect('tools:tool_detail', tool_id=tool.id)
        else:
            messages.error(request, "Please fill in all required fields correctly.")
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/add_review.html', {
        'form': form,
        'tool': tool,
        'existing': bool(review)
    })

def reviews_dashboard(request):
    tools_with_reviews = Tool.objects.filter(reviews__isnull=False).distinct()
    return render(request, 'reviews/reviews_dashboard.html', {'tools': tools_with_reviews})

def tool_reviews(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)
    return render(request, 'reviews/tool_reviews.html', {'tool': tool})
