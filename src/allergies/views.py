from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
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
        try:
            if self.serializer_class.Meta.model.objects.filter(is_active=True,slug=slug).first():
                response = self.serializer_class(self.serializer_class.Meta.model.objects.filter(is_active=True,slug=slug).first())
                return Response(response.data,status=status.HTTP_200_OK)
            elif self.serializer_class.Meta.model.objects.filter(is_active=True,pk=slug).first():
                response = self.serializer_class(self.serializer_class.Meta.model.objects.filter(is_active=True,pk=slug).first())
                return Response(response.data,status=status.HTTP_200_OK)
            return Response({'data':'not found'},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'data':'not found'},status=status.HTTP_404_NOT_FOUND)
            
class AllergiesUpdateApiView(UpdateAPIView):
    serializer_class=AllergiesCreateSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True).first()
    permission_classes = (AllowAny,)
    
    def update(self, request,pk:str, *args, **kwargs):
        try:
            if self.serializer_class.Meta.model.objects.filter(is_active=True,slug=pk).first():
                allergie = self.serializer_class(self.serializer_class.Meta.model.objects.filter(is_active=True,slug=pk).first(),data=request.data)
                if allergie.is_valid():
                    allergie.save()
                    data =  self.serializer_class.Meta.model.objects.filter(is_active=True,slug=pk).first()
                    data.update_slug()
                    data.save()
                    respose = AllergiesListSerializer(data)
                    return Response(respose.data,status=status.HTTP_200_OK)
                return Response(allergie.error_messages,status=status.HTTP_400_BAD_REQUEST)
            elif self.serializer_class.Meta.model.objects.filter(is_active=True,pk=pk).first():
                allergie = self.serializer_class(self.serializer_class.Meta.model.objects.filter(is_active=True,pk=pk).first(),data=request.data)
                if allergie.is_valid():
                    allergie.save()
                    data =  self.serializer_class.Meta.model.objects.filter(is_active=True,pk=pk).first()
                    data.update_slug()
                    data.save()
                    respose = AllergiesListSerializer(data)
                    return Response(respose.data,status=status.HTTP_200_OK)
                return Response(allergie.error_messages,status=status.HTTP_400_BAD_REQUEST)
            return Response({'data':'not found'},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'data':'not found'},status=status.HTTP_404_NOT_FOUND)

class AllergiesDestroyApiView(DestroyAPIView):
    serializer_class = AllergiesListSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True).first()
    permission_classes = (AllowAny,)
    
    def destroy(self, request, pk:str,*args, **kwargs):
        try:
            if self.serializer_class.Meta.model.objects.filter(is_active = True,slug=pk).first():
                allergi = self.serializer_class.Meta.model.objects.filter(is_active = True,slug=pk).first()
                allergi.is_active = False
                allergi.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            elif self.serializer_class.Meta.model.objects.filter(is_active = True,pk=pk).first():
                allergi = self.serializer_class.Meta.model.objects.filter(is_active = True,pk=pk).first()
                allergi.is_active = False
                allergi.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response({'data':'not found'},status=status.HTTP_404_NOT_FOUND)
        except :
            return Response({'data':'not found'},status=status.HTTP_404_NOT_FOUND)