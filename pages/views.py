from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from .models import Page, Category, Tag


class LandingPageView(TemplateView):
    template_name = 'pages/landing.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['recent_pages'] = Page.objects.filter(is_published=True)[:5]
        return context


class PageListView(ListView):
    model = Page
    template_name = 'pages/home.html'
    context_object_name = 'pages'
    paginate_by = 10
    
    def get_queryset(self):
        return Page.objects.filter(is_published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['recent_pages'] = Page.objects.filter(is_published=True)[:5]
        return context


class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/detail.html'
    context_object_name = 'page'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_queryset(self):
        return Page.objects.filter(is_published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_pages'] = Page.objects.filter(
            is_published=True,
            category=self.object.category
        ).exclude(id=self.object.id)[:3]
        return context


class CategoryListView(ListView):
    model = Page
    template_name = 'pages/category.html'
    context_object_name = 'pages'
    paginate_by = 10
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Page.objects.filter(is_published=True, category=self.category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.all()
        return context


class TagListView(ListView):
    model = Page
    template_name = 'pages/tag.html'
    context_object_name = 'pages'
    paginate_by = 10
    
    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Page.objects.filter(is_published=True, tags=self.tag)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        context['tags'] = Tag.objects.all()
        return context


class SearchView(ListView):
    model = Page
    template_name = 'pages/search.html'
    context_object_name = 'pages'
    paginate_by = 10
    
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Page.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(meta_description__icontains=query),
                is_published=True
            )
        return Page.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
