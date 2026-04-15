from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('blog/<int:id>/', blog_detail, name='blog_detail'),
    path('create/', create_blog, name='create_blog'),
]