from rest_framework import viewsets
from .models import FavoriteCharacter
from .serializers import FavoriteCharacterSerializer

class FavoriteCharacterViewSet(viewsets.ModelViewSet):
    """
    ViewSet that provides the standard actions for managing favorite characters.
    Endpoints:
    - GET /api/favorites/          -> List all favorites
    - POST /api/favorites/         -> Save a new favorite
    - GET /api/favorites/{id}/     -> Details of a favorite
    - PATCH /api/favorites/{id}/   -> Update the notes or fields of a favorite
    - DELETE /api/favorites/{id}/  -> Remove from favorites
    """
    queryset = FavoriteCharacter.objects.all().order_by('-created_at')
    serializer_class = FavoriteCharacterSerializer
