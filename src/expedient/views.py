from rest_framework.generics import ListCreateAPIView
from .serializer import ExpedietSerializer
# Create your views here.

class ExpedientListCreateView(ListCreateAPIView):
    serializer_class=ExpedietSerializer
    queryset=ExpedietSerializer.Meta.model.objects.all()
