"""flat api urls"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import api_root
from . import room_views
from . import auth_views
from flat.filters import room_filters

urlpatterns = [
    path('', api_root),
    path('rooms/', room_views.RoomList.as_view(), name='room-list'),
    path('rooms/<int:pk>/', room_views.RoomDetail.as_view(), name='room-detail'),
    path('users/', auth_views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', auth_views.UserDetail.as_view(), name='user-detail'),
    path('rooms/user', room_filters.UserRoomList.as_view(), name='user-rooms'),
    path(
        'rooms/advanced_search',
        room_filters.RoomList.as_view(),
        name='advanced-room-search'),
    path(
        'rooms/search',
        room_filters.MultipleFieldsQueryListView.as_view(),
        name='multiple-fields-search'
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
