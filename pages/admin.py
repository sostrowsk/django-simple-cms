from django.contrib import admin
from .models import Page, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'is_published', 'created_at', 'updated_at']
    list_filter = ['is_published', 'created_at', 'category', 'tags']
    search_fields = ['title', 'content', 'meta_description']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'category', 'tags')
        }),
        ('Content', {
            'fields': ('content', 'meta_description')
        }),
        ('Publishing', {
            'fields': ('is_published',)
        }),
    )
    
    filter_horizontal = ('tags',)
    
    def save_model(self, request, obj, form, change):
        if not change:  # If creating new page
            obj.author = request.user
        super().save_model(request, obj, form, change)
