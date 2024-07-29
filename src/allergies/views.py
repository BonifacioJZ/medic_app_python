from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView
from .serializers import AllergiesListSerializer,AllergiesCreateSerializer,AllergiesReatriveSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class AllergiesListApiView(ListAPIView):
    serializer_class = AllergiesListSerializer
    queryset= AllergiesListSerializer.Meta.model.objects.order_by('name').filter(is_active =True).all()
    permission_classes = (AllowAny,)
class AllergiesCreateApiView(CreateAPIView):
    serializer_class = AllergiesCreateSerializer
    queryset = AllergiesCreateSerializer.Meta.model.objects.filter(is_active = True).all()
    permission_classes=(AllowAny,)

class AllergiesRetriveApiView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AllergiesReatriveSerializer
    queryset=AllergiesReatriveSerializer.Meta.model.objects.filter(is_active = True).all()
    
    def get(self, request, slug,*args, **kwargs):
        allergies = self.serializer_class.Meta.model.objects.filter(is_active=True,slug=slug).first()
        if allergies:
            response = self.serializer_class(allergies)
            return Response(response.data,status=status.HTTP_200_OK)
        return Response({'data':'not found'},status=status.HTTP_404_NOT_FOUND)