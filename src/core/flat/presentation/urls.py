"""flat api urls"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import room_views

urlpatterns = [
    path('rooms/', room_views.room_list),
    path('rooms/<int:pk>/', room_views.room_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)