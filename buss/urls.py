from django.urls import path
from buss import views

urlpatterns = [
    path('', views.Homepage, name = 'Homepage'),
    path('MaBussines', views.Analysis,name = 'MaBussines'),
]