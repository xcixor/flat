from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .room_views import views as room_views
from .auth import views as auth_views

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'rooms': reverse('room-list', request=request, format=format),
        'user-rooms': reverse('user-rooms', request=request, format=format),
        'advanced-room-search': reverse('advanced-room-search', request=request, format=format),
        'multiple-fields-search': reverse('multiple-fields-search', request=request, format=format),
    })