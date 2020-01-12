"""flat api urls"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import room_views

urlpatterns = [
    path('rooms/', room_views.RoomList.as_view()),
    path('rooms/<int:pk>/', room_views.RoomDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)