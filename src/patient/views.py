from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.response import Response
from .models import Familiar,Patient
from .serializers import FamialiarSerializer,PatientSerializer,FamiliarDetailsSerializer
from .serializers import PatientDetailsSerializer,PatientUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from src.permissons.permissons import IsSuperuser,HasGroupPermission
from rest_framework.viewsets import ModelViewSet

class FamiliarApiView(ModelViewSet):
    """
    Esta clase proporciona una vista de la API que permite listar y crear instancias del modelo Familiar.
    
    Hereda de ListCreateAPIView que proporciona las operaciones GET (para listar objetos) y POST (para crear un nuevo objeto).
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (IsAuthenticated,HasGroupPermission|IsSuperuser,)
    permission_groups = {
        'create':['Nurses','Doctor']
    }
    
    # Define el queryset que se utilizará para obtener los datos del modelo Familiar.
    # Ordena los resultados por el campo 'first_name'.
    queryset = Familiar.objects.all().order_by('first_name')
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo Familiar
    # a y desde representaciones de datos como JSON.
    serializer_class = FamialiarSerializer
    
    def update(self, request,pk=None):
        serializer = FamialiarSerializer
        queryset = self.get_serializer().Meta.model.objects.all().filter(pk=pk).first()
        
        familiar_instance = queryset(pk)
        if familiar_instance:
            familiar_serializer = serializer(familiar_instance, data=request.data)
            if familiar_serializer.is_valid():
                familiar_serializer.save()
                return Response(familiar_serializer.data, status=status.HTTP_200_OK)
            return Response(familiar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Objeto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        
class FamiliarDestroyApiView(DestroyAPIView):
    """
    Esta clase proporciona una vista de la API que permite eliminar (desactivar) una instancia específica del modelo Familiar.
    
    Hereda de DestroyAPIView que proporciona la operación DELETE para eliminar un objeto.
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (IsAuthenticated,IsSuperuser)
    
    # Define el queryset que se utilizará para obtener los datos del modelo Familiar.
    queryset = Familiar.objects.all()
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo Familiar
    # a y desde representaciones de datos como JSON.
    serializer_class = FamialiarSerializer
    
    def get_queryset(self, pk: str):
        """
        Obtiene el queryset filtrado por la clave primaria (pk) especificada.
        
        Args:
            pk (str): La clave primaria de la instancia del modelo.
        
        Returns:
            QuerySet: Un queryset con la instancia del modelo filtrada por la clave primaria.
        """
        return self.serializer_class.Meta.model.objects.filter(pk=pk).first()
    
    def delete(self, request, pk: str, *args, **kwargs):
        """
        Desactiva la instancia del modelo especificada.
        
        Args:
            request (Request): La solicitud que contiene los datos para eliminar.
            pk (str): La clave primaria de la instancia del modelo a desactivar.
        
        Returns:
            Response: Una respuesta HTTP con un mensaje de éxito o un error 404 si la instancia no se encuentra.
        """
        familiar = self.get_queryset(pk)
        if familiar:
            familiar.is_active = False
            familiar.save()
            return Response({"message": "deleted"}, status=status.HTTP_204_NO_CONTENT)
        
        return Response(status=status.HTTP_404_NOT_FOUND)


class PatientApiView(ModelViewSet):
    """
    Esta clase proporciona una vista de la API que permite listar y crear instancias del modelo Patient.
    
    Hereda de ListCreateAPIView que proporciona las operaciones GET (para listar objetos) y POST (para crear un nuevo objeto).
    """
    serializer_class = FamialiarSerializer
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (IsAuthenticated,HasGroupPermission|IsSuperuser,)
    permission_groups = {
        'create':['Nurses','Doctor']
    }


class PatientUpdateApiView(UpdateAPIView):
    """
    Esta clase proporciona una vista de la API que permite actualizar una instancia específica del modelo Patient.
    
    Hereda de UpdateAPIView que proporciona la operación PUT para actualizar un objeto.
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (IsAuthenticated,IsSuperuser,)
    
    # Define el queryset que se utilizará para obtener los datos del modelo Patient.
    queryset = Patient.objects.all()
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo Patient
    # a y desde representaciones de datos como JSON.
    serializer_class = PatientUpdateSerializer
    
    def get_queryset(self, pk: str = None):
        """
        Obtiene el queryset filtrado por la clave primaria (pk) especificada.
        
        Args:
            pk (str): La clave primaria de la instancia del modelo Patient.
        
        Returns:
            QuerySet: Un queryset con la instancia del modelo Patient filtrada por la clave primaria.
        """
        return self.get_serializer().Meta.model.objects.all().filter(pk=pk).first()
    
    def put(self, request, pk: str = None, *args, **kwargs):
        """
        Actualiza la instancia del modelo Patient especificada.
        
        Args:
            request (Request): La solicitud que contiene los datos para actualizar.
            pk (str): La clave primaria de la instancia del modelo Patient a actualizar.
        
        Returns:
            Response: Una respuesta HTTP con los datos actualizados o los errores de validación.
        """
        patient_instance = self.get_queryset(pk)
        if patient_instance:
            patient_serializer = self.serializer_class(patient_instance, data=request.data)
            if patient_serializer.is_valid():
                patient_serializer.save()
                return Response(patient_serializer.data, status=status.HTTP_200_OK)
            return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Objeto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

                

class PatientDestroyApiView(DestroyAPIView):
    """
    Esta clase proporciona una vista de la API que permite eliminar (desactivar) una instancia específica del modelo Patient.
    
    Hereda de DestroyAPIView que proporciona la operación DELETE para eliminar un objeto.
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (IsAuthenticated,IsSuperuser)
    
    # Define el queryset que se utilizará para obtener los datos del modelo Patient.
    queryset = Patient.objects.all()
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo Patient
    # a y desde representaciones de datos como JSON.
    serializer_class = PatientSerializer
    
    def get_queryset(self, pk: str):
        """
        Obtiene el queryset filtrado por la clave primaria (pk) especificada.
        
        Args:
            pk (str): La clave primaria de la instancia del modelo.
        
        Returns:
            QuerySet: Un queryset con la instancia del modelo filtrada por la clave primaria.
        """
        return self.serializer_class.Meta.model.objects.filter(pk=pk).first()
    
    def delete(self, request, pk: str, *args, **kwargs):
        """
        Desactiva la instancia del modelo especificada.
        
        Args:
            request (Request): La solicitud que contiene los datos para eliminar.
            pk (str): La clave primaria de la instancia del modelo a desactivar.
        
        Returns:
            Response: Una respuesta HTTP con un mensaje de éxito o un error 404 si la instancia no se encuentra.
        """
        patient = self.get_queryset(pk)
        
        if patient:
            patient.is_active = False
            patient.save()
            return Response({"message": "deleted"}, status=status.HTTP_204_NO_CONTENT)
        
        return Response(status=status.HTTP_404_NOT_FOUND)
