from django.urls import path
from . import views

urlpatterns= [
    path('',views.index, name = 'slide'),
    path('slideNext/',views.slideNext, name='slideNext'),
        
]