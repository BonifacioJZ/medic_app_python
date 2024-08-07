from rest_framework.generics import DestroyAPIView,UpdateAPIView,ListAPIView,CreateAPIView,RetrieveAPIView
from .serializer import ExpedientSerializer,ListExpedietSerializer,CreateExpedientSerializer,ExpedientDetailsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_guardian import filters
from  rest_framework import status
from rest_framework.response import Response
from src.permissons.permissons import CustomObjectPermissions,IsUserActive
# Create your views here.

class ExpedientListApiView(ListAPIView):
    """
    Esta clase proporciona una vista de la API que permite listar todas las instancias activas del modelo asociado.
    
    Hereda de ListAPIView que proporciona la operación GET para listar objetos.
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (CustomObjectPermissions,IsUserActive,)
    filter_backends = [filters.ObjectPermissionsFilter]
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo
    # a y desde representaciones de datos como JSON.
    serializer_class = ListExpedietSerializer
    
    # Define el queryset que se utilizará para obtener los datos del modelo.
    # Filtra las instancias para incluir solo aquellas que están activas (is_active=True) y utiliza prefetch_related para optimizar las consultas de relaciones.
    queryset = ListExpedietSerializer.Meta.model.objects.all().filter(is_active=True).prefetch_related()

    
class ExpedientCreateApiView(CreateAPIView):
    """
    Esta clase proporciona una vista de la API que permite crear una nueva instancia del modelo asociado.
    
    Hereda de CreateAPIView que proporciona la operación POST para crear un nuevo objeto.
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (CustomObjectPermissions,IsUserActive,)
    filter_backends = [filters.ObjectPermissionsFilter]
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo
    # a y desde representaciones de datos como JSON.
    serializer_class = CreateExpedientSerializer
    
    # Define el queryset que se utilizará para obtener los datos del modelo.
    queryset = CreateExpedientSerializer.Meta.model.objects.all()
    
    def post(self, request, *args, **kwargs):
        """
        Maneja las solicitudes POST para crear una nueva instancia del modelo.
        
        Args:
            request (Request): La solicitud que contiene los datos para crear el objeto.
        
        Returns:
            Response: Una respuesta HTTP con los datos del nuevo objeto creado o los errores de validación.
        """
        user = request.user
        instance = self.serializer_class(data=request.data)
        if instance.is_valid():
            instance.save(user=user)
            return Response(data=instance.data, status=status.HTTP_201_CREATED)
        return Response(data=instance.errors, status=status.HTTP_400_BAD_REQUEST)


    
class ExpedientRetrieveViewApiView(RetrieveAPIView):
    """
    Esta clase proporciona una vista de la API que permite recuperar (obtener) una instancia específica y activa del modelo asociado.
    
    Hereda de RetrieveAPIView que proporciona la operación GET para obtener un solo objeto.
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (CustomObjectPermissions,IsUserActive,)
    filter_backends = [filters.ObjectPermissionsFilter]
    
    # Define la clase de serializador que se utilizará para convertir la instancia del modelo
    # a y desde representaciones de datos como JSON.
    serializer_class = ExpedientDetailsSerializer
    
    # Define el queryset que se utilizará para obtener los datos del modelo.
    # Selecciona las instancias relacionadas para optimizar las consultas y filtra las instancias para incluir solo aquellas que están activas (is_active=True).
    queryset = ExpedientDetailsSerializer.Meta.model.objects.select_related().all().filter(is_active=True)
class ExpedientUpdateApiView(UpdateAPIView):
    """
    Esta clase proporciona una vista de la API que permite actualizar una instancia específica del modelo asociado.
    
    Hereda de UpdateAPIView que proporciona la operación PUT para actualizar un objeto.
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (CustomObjectPermissions,IsUserActive,)
    filter_backends = [filters.ObjectPermissionsFilter]
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo
    # a y desde representaciones de datos como JSON.
    serializer_class = CreateExpedientSerializer
    
    # Define el queryset que se utilizará para obtener los datos del modelo.
    queryset = CreateExpedientSerializer.Meta.model.objects.all()


class ExpedientDestroyApiView(DestroyAPIView):
    """
    Esta clase proporciona una vista de la API que permite "eliminar" (desactivar) una instancia específica del modelo asociado.
    
    Hereda de DestroyAPIView que proporciona la operación DELETE para eliminar un objeto.
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    # Se comenta la línea de permisos para que el código funcione sin restricciones de autenticación. 
    # Descomentar la siguiente línea para exigir autenticación:
    permission_classes = (CustomObjectPermissions,IsUserActive,)
    filter_backends = [filters.ObjectPermissionsFilter]
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo
    # a y desde representaciones de datos como JSON.
    serializer_class = ExpedientSerializer
    
    # Define el queryset que se utilizará para obtener los datos del modelo.
    queryset = ExpedientSerializer.Meta.model.objects.all()
    
    
    def delete(self, request, pk: str, *args, **kwargs):
        """
        Desactiva la instancia del modelo especificada.
        
        Args:
            request (Request): La solicitud que contiene los datos para eliminar.
            pk (str): La clave primaria de la instancia del modelo a desactivar.
        
        Returns:
            Response: Una respuesta HTTP con un mensaje de éxito o un error 404 si la instancia no se encuentra.
        """
        expedient = self.serializer_class.Meta.model.objects.filter(pk=pk,is_active=True).first()
        
        if expedient:
            expedient.is_active = False
            expedient.save()
            return Response({"message": "deleted"}, status=status.HTTP_204_NO_CONTENT)
        
        return Response(status=status.HTTP_404_NOT_FOUND)

