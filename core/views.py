from rest_framework.viewsets import ModelViewSet
from core.serializer import NoteSerializer
from core.models import Note

# Create your views here.

class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    http_method_names = ['post']
