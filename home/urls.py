from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogList.as_view(), name='home'),
    path('<slug:slug>/', views.blogDetail.as_view(), name='blog_detail'),
    path('about.html/', views.about, name='about'),
    path('contact.html/', views.contact, name='contact'),
    path('editor.html/', views.editor.as_view(), name='editor'),
]