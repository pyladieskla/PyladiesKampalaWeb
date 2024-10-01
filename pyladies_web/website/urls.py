from django.urls import path
from . import views

urlpatterns = [
    path('website/', views.website1, name='website1'),
    # path('index/', views.members, name='websiteindex'),
    path("", views.website, name='website'),
]
