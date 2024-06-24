from rest_framework.generics import ListAPIView
from .models import Familiar,Patient
from .serializers import FamialiarListSerializer,PatientListSerializer

class FamiliarListApiView(ListAPIView):
    queryset= Familiar.objects.all().order_by('first_name')
    serializer_class= FamialiarListSerializer

class PatientListApiView(ListAPIView):
    queryset= Patient.objects.all().order_by('first_name')
    serializer_class=PatientListSerializer     