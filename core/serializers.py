from rest_framework import serializers
from .models import FavoriteCharacter

class FavoriteCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCharacter
        fields = [
            'id',            # internal ID
            'external_id',   # Rick & Morty API character ID
            'name',
            'status',
            'species',
            'image_url',
            'notes',         # Your notes about the character
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']
