from django.db import models


class FavoriteCharacter(models.Model):
    external_id = models.IntegerField(unique=True)

    name = models.CharField(max_length=150)
    status = models.CharField(max_length=50)
    species = models.CharField(max_length=100)
    image_url = models.URLField(max_length=500)

    notes = models.TextField(blank=True, null=True, help_text="You can add your personal notes about this character here.")
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (ID API: {self.external_id})"
