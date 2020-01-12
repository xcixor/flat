"""Room models."""
from django.db import models


ROOM_CHOICES = (
    ("single", "Single"),
    ("double", "Double"),
    ("bedsitter", "Bedsitter"),
    ("1 bedroom", "1 Bedroom"),
    ("custom", "Custom")
    )


class Room(models.Model):
    """Represents a room"""
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=600, blank=False, null=False)
    location = models.CharField(max_length=100, blank=True, default='')
    price = models.IntegerField()
    room_type = models.CharField(
        choices=ROOM_CHOICES,
        default='Single', max_length=100
        )
    image = models.ImageField(null=True, upload_to="images/room/images/")
    owner = models.ForeignKey(
        'auth.User',
        related_name='rooms',
        on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
