from rest_framework import serializers
from .models import Playlist

class song_serializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist