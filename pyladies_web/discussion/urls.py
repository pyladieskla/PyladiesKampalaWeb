from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.discussion, name='discussion'),
]