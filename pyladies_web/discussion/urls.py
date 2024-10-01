from django.urls import path
from . import views

urlpatterns = [
        path("", views.discussion, name='discussion'),
        path('addInForum/',addInForum,name='addInForum'),
        path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
]