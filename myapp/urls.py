from django.urls import path
from myapp import views
from myapp.views import services

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),
    path('blogs',views.blogs,name='blogs'),
    path('help',views.help,name='help'),
]