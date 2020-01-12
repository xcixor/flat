"""flat api urls"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import api_root
from . import room_views
from . import auth_views

urlpatterns = [
    path('', api_root),
    path('rooms/', room_views.RoomList.as_view(), name='room-list'),
    path('rooms/<int:pk>/', room_views.RoomDetail.as_view(), name='room-detail'),
    path('users/', auth_views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', auth_views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
