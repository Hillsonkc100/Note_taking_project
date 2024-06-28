from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ("title",)