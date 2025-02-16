#region Declarations

from django.db import models

#endregion

#region Dropdown Models

class Artist(models.Model):
    code = models.CharField(max_length=12, null=False, blank=False, default="100")
    desc = models.CharField(max_length=240, default="UNKNOWN")

    class Meta:
        managed = False

    def __str__(self):
        return self.code

class Genre(models.Model):
    code = models.CharField(max_length=12, null=False, blank=False, default="100")
    desc = models.CharField(max_length=240, default="UNKNOWN")

    class Meta:
        managed = False

    def __str__(self):
        return self.code

#endregion

#region Playlist 

class Playlist(models.Model):
    link = models.URLField(max_length=4000, null=False, blank=False)
    playlist_name = models.CharField(max_length=240)
    curated_artists = models.ManyToManyField('Artist') 
    genre = models.ManyToManyField('Genre')
    songs_count = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=12)

    def __str__(self):
        return self.playlist_name

    class Meta:
        managed = False
        ordering = ['-created_at']  

#endregion