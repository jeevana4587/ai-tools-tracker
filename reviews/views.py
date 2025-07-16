from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponseForbidden
from django.core.paginator import Paginator
from django.db.models import Q, Avg, Count, F
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

from tools.models import Tool
from .models import Review, ReviewHelpfulVote, ReviewReport
from .forms import ReviewForm, ReviewReportForm, ReviewFilterForm


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
            review_obj = form.save(commit=False)
            review_obj.user = request.user
            review_obj.tool = tool
            review_obj.save()
            
            action = "updated" if review else "submitted"
            messages.success(request, f"Your review has been {action} successfully.")
            return redirect('reviews:tool_reviews', tool_id=tool.id)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/add_review.html', {
        'form': form,
        'tool': tool,
        'existing': bool(review)
    })

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    
    # Check if user owns this review
    if review.user != request.user:
        messages.error(request, "You can only edit your own reviews.")
        return redirect('reviews:tool_reviews', tool_id=review.tool.id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been updated successfully.")
            return redirect('reviews:tool_reviews', tool_id=review.tool.id)
    else:
        form = ReviewForm(instance=review)
    
    return render(request, 'reviews/edit_review.html', {
        'form': form,
        'review': review,
        'tool': review.tool
    })

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    
    # Check if user owns this review
    if review.user != request.user:
        messages.error(request, "You can only delete your own reviews.")
        return redirect('reviews:tool_reviews', tool_id=review.tool.id)
    
    if request.method == 'POST':
        tool_id = review.tool.id
        review.delete()
        messages.success(request, "Your review has been deleted.")
        return redirect('reviews:tool_reviews', tool_id=tool_id)
    
    return render(request, 'reviews/delete_review.html', {
        'review': review
    })

def reviews_dashboard(request):
    # Get featured reviews
    featured_reviews = Review.objects.filter(
        is_featured=True, 
        is_approved=True
    ).select_related('user', 'tool')[:6]
    
    # Get recent reviews
    recent_reviews = Review.objects.filter(
        is_approved=True
    ).select_related('user', 'tool').order_by('-created_at')[:10]
    
    # Get tools with most reviews
    popular_tools = Tool.objects.annotate(
        review_count=Count('reviews', filter=Q(reviews__is_approved=True)),
        avg_rating=Avg('reviews__stars', filter=Q(reviews__is_approved=True))
    ).filter(review_count__gt=0).order_by('-review_count')[:10]
    
    # Get top rated tools
    top_rated_tools = Tool.objects.annotate(
        review_count=Count('reviews', filter=Q(reviews__is_approved=True)),
        avg_rating=Avg('reviews__stars', filter=Q(reviews__is_approved=True))
    ).filter(review_count__gte=3).order_by('-avg_rating')[:10]
    
    context = {
        'featured_reviews': featured_reviews,
        'recent_reviews': recent_reviews,
        'popular_tools': popular_tools,
        'top_rated_tools': top_rated_tools,
    }
    
    return render(request, 'reviews/reviews_dashboard.html', context)

def tool_reviews(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)
    
    # Get filter form
    filter_form = ReviewFilterForm(request.GET)
    
    # Base queryset - only approved reviews
    reviews = Review.objects.filter(
        tool=tool, 
        is_approved=True
    ).select_related('user').prefetch_related('helpful_votes')
    
    # Apply filters
    if filter_form.is_valid():
        sort_by = filter_form.cleaned_data.get('sort_by', 'newest')
        rating_filter = filter_form.cleaned_data.get('rating_filter', 'all')
        verified_only = filter_form.cleaned_data.get('verified_only', False)
        
        # Rating filter
        if rating_filter and rating_filter != 'all':
            reviews = reviews.filter(stars=int(rating_filter))
        
        # Verified filter
        if verified_only:
            reviews = reviews.filter(is_verified=True)
        
        # Sorting
        if sort_by == 'oldest':
            reviews = reviews.order_by('created_at')
        elif sort_by == 'highest_rated':
            reviews = reviews.order_by('-stars', '-created_at')
        elif sort_by == 'lowest_rated':
            reviews = reviews.order_by('stars', '-created_at')
        elif sort_by == 'most_helpful':
            reviews = reviews.annotate(
                helpful_count=Count('helpful_votes', filter=Q(helpful_votes__is_helpful=True))
            ).order_by('-helpful_count', '-created_at')
        else:  # newest (default)
            reviews = reviews.order_by('-created_at')
    else:
        reviews = reviews.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(reviews, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Calculate statistics
    stats = Review.objects.filter(tool=tool, is_approved=True).aggregate(
        total_reviews=Count('id'),
        avg_rating=Avg('stars'),
        five_star=Count('id', filter=Q(stars=5)),
        four_star=Count('id', filter=Q(stars=4)),
        three_star=Count('id', filter=Q(stars=3)),
        two_star=Count('id', filter=Q(stars=2)),
        one_star=Count('id', filter=Q(stars=1)),
    )
    
    # Check if user has already reviewed this tool
    user_review = None
    if request.user.is_authenticated:
        try:
            user_review = Review.objects.get(user=request.user, tool=tool)
        except Review.DoesNotExist:
            pass
    
    context = {
        'tool': tool,
        'reviews': page_obj,
        'filter_form': filter_form,
        'stats': stats,
        'user_review': user_review,
    }
    
    return render(request, 'reviews/tool_reviews.html', context)

@login_required
@require_POST
def vote_helpful(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    is_helpful = request.POST.get('is_helpful') == 'true'
    
    # Check if user is trying to vote on their own review
    if review.user == request.user:
        return JsonResponse({'error': 'You cannot vote on your own review'}, status=400)
    
    vote, created = ReviewHelpfulVote.objects.get_or_create(
        review=review,
        user=request.user,
        defaults={'is_helpful': is_helpful}
    )
    
    if not created:
        # Update existing vote
        if vote.is_helpful != is_helpful:
            vote.is_helpful = is_helpful
            vote.save()
            action = 'updated'
        else:
            # Same vote, remove it
            vote.delete()
            action = 'removed'
    else:
        action = 'added'
    
    # Return updated counts
    helpful_count = review.helpful_votes_count
    not_helpful_count = review.not_helpful_votes_count
    
    return JsonResponse({
        'helpful_count': helpful_count,
        'not_helpful_count': not_helpful_count,
        'action': action
    })

@login_required
def report_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    
    # Check if user is trying to report their own review
    if review.user == request.user:
        messages.error(request, "You cannot report your own review.")
        return redirect('reviews:tool_reviews', tool_id=review.tool.id)
    
    # Check if user has already reported this review
    if ReviewReport.objects.filter(review=review, reporter=request.user).exists():
        messages.warning(request, "You have already reported this review.")
        return redirect('reviews:tool_reviews', tool_id=review.tool.id)
    
    if request.method == 'POST':
        form = ReviewReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.review = review
            report.reporter = request.user
            report.save()
            messages.success(request, "Thank you for reporting this review. We will investigate it.")
            return redirect('reviews:tool_reviews', tool_id=review.tool.id)
    else:
        form = ReviewReportForm()
    
    return render(request, 'reviews/report_review.html', {
        'form': form,
        'review': review
    })

def review_analytics(request):
    """Analytics dashboard for reviews"""
    if not request.user.is_staff:
        return HttpResponseForbidden()
    
    # Overall statistics
    total_reviews = Review.objects.count()
    approved_reviews = Review.objects.filter(is_approved=True).count()
    pending_reviews = Review.objects.filter(is_approved=False).count()
    verified_reviews = Review.objects.filter(is_verified=True).count()
    featured_reviews = Review.objects.filter(is_featured=True).count()
    
    # Rating distribution
    rating_stats = Review.objects.filter(is_approved=True).values('stars').annotate(
        count=Count('id')
    ).order_by('stars')
    
    # Recent activity
    recent_reports = ReviewReport.objects.filter(
        is_resolved=False
    ).select_related('review', 'reporter').order_by('-created_at')[:10]
    
    # Top reviewers
    top_reviewers = Review.objects.filter(is_approved=True).values('user__username').annotate(
        review_count=Count('id'),
        avg_rating=Avg('stars')
    ).order_by('-review_count')[:10]
    
    context = {
        'total_reviews': total_reviews,
        'approved_reviews': approved_reviews,
        'pending_reviews': pending_reviews,
        'verified_reviews': verified_reviews,
        'featured_reviews': featured_reviews,
        'rating_stats': rating_stats,
        'recent_reports': recent_reports,
        'top_reviewers': top_reviewers,
    }
    
    return render(request, 'reviews/analytics.html', context)

@login_required
def my_reviews(request):
    """Display user's own reviews"""
    reviews = Review.objects.filter(user=request.user).select_related('tool').order_by('-created_at')
    
    paginator = Paginator(reviews, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'reviews/my_reviews.html', {
        'reviews': page_obj
    })
