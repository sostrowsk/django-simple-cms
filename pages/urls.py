from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='home'),
    path('blog/', views.PageListView.as_view(), name='blog'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('page/<slug:slug>/', views.PageDetailView.as_view(), name='page_detail'),
    path('category/<slug:slug>/', views.CategoryListView.as_view(), name='category_detail'),
    path('tag/<slug:slug>/', views.TagListView.as_view(), name='tag_detail'),
]