from django.contrib import admin
from django.urls import path
from .views import (
    blog_post_detail_view,
    blog_post_list_page,
    blog_post_create_page,
    blog_post_update_page,
    blog_post_delete_page
)

urlpatterns = [ 
    path('', blog_post_list_page), 
    path('<str:slug>/', blog_post_detail_view), 
    path('<str:slug>/edit/', blog_post_update_page), 
    path('<str:slug>/delete/', blog_post_delete_page), 
]