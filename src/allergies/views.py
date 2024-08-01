from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from .serializers import AllergiesListSerializer,AllergiesCreateSerializer,AllergiesReatriveSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_guardian.filters import ObjectPermissionsFilter
from src.permissons.permissons import CustomObjectPermissions,IsUserActive

# Create your views here.
class AllergiesListApiView(ListAPIView):
    """
    Esta clase proporciona una vista de la API que permite listar todas las instancias activas del modelo de alergias.
    
    Hereda de ListAPIView que proporciona la operación GET para listar objetos.
    """
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo
    # a y desde representaciones de datos como JSON.
    serializer_class = AllergiesListSerializer
    
    # Define el queryset que se utilizará para obtener los datos del modelo de alergias.
    queryset = AllergiesListSerializer.Meta.model.objects.order_by('name').filter(is_active=True).all()
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (CustomObjectPermissions, IsUserActive,)
    
    # Define los backends de filtro que se utilizarán para filtrar los datos de acuerdo con los permisos de objeto.
    filter_backends = [ObjectPermissionsFilter,]
    
class AllergiesCreateApiView(CreateAPIView):
    """
    Esta clase proporciona una vista de la API que permite crear una nueva instancia del modelo de alergias.
    
    Hereda de CreateAPIView que proporciona la operación POST para crear un nuevo objeto.
    """
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo
    # a y desde representaciones de datos como JSON.
    serializer_class = AllergiesCreateSerializer
    
    # Define el queryset que se utilizará para obtener los datos del modelo de alergias.
    queryset = AllergiesCreateSerializer.Meta.model.objects.filter(is_active=True).all()
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (CustomObjectPermissions, IsUserActive,)
    
    # Define los backends de filtro que se utilizarán para filtrar los datos de acuerdo con los permisos de objeto.
    filter_backends = [ObjectPermissionsFilter,]
    
    def post(self, request, *args, **kwargs):
        """
        Maneja las solicitudes POST para crear una nueva instancia del modelo de alergias.
        
        Args:
            request (Request): La solicitud que contiene los datos para crear el objeto.
        
        Returns:
            Response: Una respuesta HTTP con los datos del nuevo objeto creado o los errores de validación.
        """
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            data.save()
            allergie = self.serializer_class.Meta.model.objects.filter(pk=data.data['id']).first()
            response = AllergiesListSerializer(allergie)
            return Response(response.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class AllergiesRetriveApiView(RetrieveAPIView):
    """
    Esta clase proporciona una vista de la API que permite recuperar una instancia específica del modelo de alergias.
    
    Hereda de RetrieveAPIView que proporciona la operación GET para recuperar un objeto.
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (CustomObjectPermissions, IsUserActive,)
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo
    # a y desde representaciones de datos como JSON.
    serializer_class = AllergiesReatriveSerializer
    
    # Define el queryset que se utilizará para obtener los datos del modelo de alergias.
    queryset = serializer_class.Meta.model.objects.select_related().filter(is_active=True).all()
    
    # Define los backends de filtro que se utilizarán para filtrar los datos de acuerdo con los permisos de objeto.
    filter_backends = [ObjectPermissionsFilter,]
    
    def get(self, request, slug, *args, **kwargs):
        """
        Maneja las solicitudes GET para recuperar una instancia específica del modelo de alergias.
        
        Args:
            request (Request): La solicitud que contiene los datos para recuperar el objeto.
            slug (str): El identificador único (slug o clave primaria) de la instancia del modelo.
        
        Returns:
            Response: Una respuesta HTTP con los datos del objeto recuperado o un mensaje de error.
        """
        try:
            # Intenta encontrar la instancia del modelo por el slug
            instance = self.serializer_class.Meta.model.objects.filter(is_active=True, slug=slug).first()
            if instance:
                response = self.serializer_class(instance)
                return Response(response.data, status=status.HTTP_200_OK)
            
            # Si no se encuentra por el slug, intenta encontrarla por la clave primaria (pk)
            instance = self.serializer_class.Meta.model.objects.filter(is_active=True, pk=slug).first()
            if instance:
                response = self.serializer_class(instance)
                return Response(response.data, status=status.HTTP_200_OK)
            
            # Si no se encuentra la instancia, devuelve un error 404
            return Response({'data': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception:
            # Maneja cualquier excepción y devuelve un error 404
            return Response({'data': 'not found'}, status=status.HTTP_404_NOT_FOUND)

class AllergiesUpdateApiView(UpdateAPIView):
    """
    Esta clase proporciona una vista de la API que permite actualizar una instancia específica del modelo de alergias.
    
    Hereda de UpdateAPIView que proporciona la operación PUT para actualizar un objeto.
    """
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo
    # a y desde representaciones de datos como JSON.
    serializer_class = AllergiesCreateSerializer
    
    # Define el queryset que se utilizará para obtener los datos del modelo de alergias.
    queryset = serializer_class.Meta.model.objects.filter(is_active=True).first()
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (CustomObjectPermissions, IsUserActive,)
    
    # Define los backends de filtro que se utilizarán para filtrar los datos de acuerdo con los permisos de objeto.
    filter_backends = [ObjectPermissionsFilter,]
    
    def update(self, request, pk: str, *args, **kwargs):
        """
        Maneja las solicitudes PUT para actualizar una instancia específica del modelo de alergias.
        
        Args:
            request (Request): La solicitud que contiene los datos para actualizar el objeto.
            pk (str): El identificador único (slug o clave primaria) de la instancia del modelo.
        
        Returns:
            Response: Una respuesta HTTP con los datos del objeto actualizado o los errores de validación.
        """
        try:
            # Intenta encontrar la instancia del modelo por el slug
            instance = self.serializer_class.Meta.model.objects.filter(is_active=True, slug=pk).first()
            if instance:
                allergie = self.serializer_class(instance, data=request.data)
                if allergie.is_valid():
                    allergie.save()
                    instance.update_slug()
                    instance.save()
                    response = AllergiesListSerializer(instance)
                    return Response(response.data, status=status.HTTP_200_OK)
                return Response(allergie.errors, status=status.HTTP_400_BAD_REQUEST)
            
            # Si no se encuentra por el slug, intenta encontrarla por la clave primaria (pk)
            instance = self.serializer_class.Meta.model.objects.filter(is_active=True, pk=pk).first()
            if instance:
                allergie = self.serializer_class(instance, data=request.data)
                if allergie.is_valid():
                    allergie.save()
                    instance.update_slug()
                    instance.save()
                    response = AllergiesListSerializer(instance)
                    return Response(response.data, status=status.HTTP_200_OK)
                return Response(allergie.errors, status=status.HTTP_400_BAD_REQUEST)
            
            # Si no se encuentra la instancia, devuelve un error 404
            return Response({'data': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception:
            # Maneja cualquier excepción y devuelve un error 404
            return Response({'data': 'not found'}, status=status.HTTP_404_NOT_FOUND)


class AllergiesDestroyApiView(DestroyAPIView):
    """
    Esta clase proporciona una vista de la API que permite eliminar (desactivar) una instancia específica del modelo de alergias.
    
    Hereda de DestroyAPIView que proporciona la operación DELETE para eliminar un objeto.
    """
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo
    # a y desde representaciones de datos como JSON.
    serializer_class = AllergiesListSerializer
    
    # Define el queryset que se utilizará para obtener los datos del modelo de alergias.
    queryset = serializer_class.Meta.model.objects.filter(is_active=True).first()
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (CustomObjectPermissions, IsUserActive,)
    
    # Define los backends de filtro que se utilizarán para filtrar los datos de acuerdo con los permisos de objeto.
    filter_backends = [ObjectPermissionsFilter,]
    
    def destroy(self, request, pk: str, *args, **kwargs):
        """
        Maneja las solicitudes DELETE para desactivar una instancia específica del modelo de alergias.
        
        Args:
            request (Request): La solicitud que contiene los datos para eliminar el objeto.
            pk (str): El identificador único (slug o clave primaria) de la instancia del modelo.
        
        Returns:
            Response: Una respuesta HTTP con el estado de la operación de eliminación.
        """
        try:
            # Intenta encontrar la instancia del modelo por el slug
            instance = self.serializer_class.Meta.model.objects.filter(is_active=True, slug=pk).first()
            if instance:
                instance.is_active = False
                instance.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            
            # Si no se encuentra por el slug, intenta encontrarla por la clave primaria (pk)
            instance = self.serializer_class.Meta.model.objects.filter(is_active=True, pk=pk).first()
            if instance:
                instance.is_active = False
                instance.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            
            # Si no se encuentra la instancia, devuelve un error 404
            return Response({'data': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception:
            # Maneja cualquier excepción y devuelve un error 404
            return Response({'data': 'not found'}, status=status.HTTP_404_NOT_FOUND)
