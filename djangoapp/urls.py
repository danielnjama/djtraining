from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("contact-us/", views.contact, name='contact'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog')
]