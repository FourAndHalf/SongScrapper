from django.db import models

class FormData(models.Model):
    name = models.TextField(max_length=100, default="Anonymous")
    title = models.TextField(max_length=400, default="Indie Boy")
    link = models.URLField(max_length=1000, default="Give it some thought")

    def __str__(self) -> str:
        return self.name