from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.postslist.as_view(), name='blog'),
    path('<slug:slug>/', views.postdetail.as_view(), name='blog_detail'),
    path('categories/<slug:slug>/', views.category_posts, name='category-posts'),
]
