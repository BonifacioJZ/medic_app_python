from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.response import Response
from .models import Familiar,Patient
from .serializers import FamialiarListSerializer,PatientListSerializer,CreateFamiliarSerializer
from rest_framework import status

class FamiliarListApiView(ListAPIView):
    queryset= Familiar.objects.all().order_by('first_name')
    serializer_class= FamialiarListSerializer

class FamiliarCreateApiView(CreateAPIView):
    serializer_class = CreateFamiliarSerializer
    
    def post(self, request, *args, **kwargs):
        serializer= CreateFamiliarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientListApiView(ListAPIView):
    queryset= Patient.objects.all().order_by('first_name')
    serializer_class=PatientListSerializer     