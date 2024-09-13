from django.urls import path
from . import views

urlpatterns = [
    # path('website/', views.website, name='website'),
    # path('index/', views.members, name='websiteindex'),
    path("", views.website, name='website'),
]
