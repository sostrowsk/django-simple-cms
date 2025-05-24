from .models import Category, Page


def global_context(request):
    """Add global context variables for templates."""
    return {
        'categories': Category.objects.all()[:5],  # Limit to 5 categories for navigation
        'recent_pages': Page.objects.filter(is_published=True).order_by('-created_at')[:5],
    }