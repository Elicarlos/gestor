from rest_framework import generics
from core.models import Cursos
from .serializers import CursosSerializer

# Create your views here.
class CursoList(generics.ListCreateAPIView):

    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer