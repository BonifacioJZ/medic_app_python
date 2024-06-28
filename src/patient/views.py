from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.response import Response
from .models import Familiar,Patient
from .serializers import FamialiarSerializer,PatientSerializer,FamiliarDetailsSerializer
from .serializers import PatientDetailsSerializer,PatientUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class FamiliarCreateListApiView(ListCreateAPIView):
    """
    Esta clase proporciona una vista de la API que permite listar y crear instancias del modelo Familiar.
    
    Hereda de ListCreateAPIView que proporciona las operaciones GET (para listar objetos) y POST (para crear un nuevo objeto).
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (IsAuthenticated,)
    
    # Define el queryset que se utilizará para obtener los datos del modelo Familiar.
    # Ordena los resultados por el campo 'first_name'.
    queryset = Familiar.objects.all().order_by('first_name')
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo Familiar
    # a y desde representaciones de datos como JSON.
    serializer_class = FamialiarSerializer


class FamiliarRetriveApiView(RetrieveAPIView):
    """
    Esta clase proporciona una vista de la API que permite recuperar (obtener) una instancia específica del modelo Familiar.
    
    Hereda de RetrieveAPIView que proporciona la operación GET para obtener un solo objeto.
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (IsAuthenticated,)
    
    # Define la clase de serializador que se utilizará para convertir la instancia del modelo Familiar
    # a y desde representaciones de datos como JSON.
    serializer_class = FamiliarDetailsSerializer
    
    # Define el queryset que se utilizará para obtener los datos del modelo Familiar.
    # Se utiliza select_related para realizar una única consulta SQL que incluya las relaciones de clave externa.
    queryset = Familiar.objects.select_related().all()

    
class FamiliarUpdateApiView(UpdateAPIView):
    """
    Esta clase proporciona una vista de la API que permite actualizar una instancia específica del modelo Familiar.
    
    Hereda de UpdateAPIView que proporciona la operación PUT para actualizar un objeto.
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (IsAuthenticated,)
    
    # Define el queryset que se utilizará para obtener los datos del modelo Familiar.
    queryset = Familiar.objects.all()
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo Familiar
    # a y desde representaciones de datos como JSON.
    serializer_class = FamialiarSerializer
    
    def get_queryset(self, pk=None):
        """
        Obtiene el queryset filtrado por la clave primaria (pk) especificada.
        
        Args:
            pk (int): La clave primaria de la instancia del modelo Familiar.
        
        Returns:
            QuerySet: Un queryset con la instancia del modelo Familiar filtrada por la clave primaria.
        """
        return self.get_serializer().Meta.model.objects.all().filter(pk=pk).first()
    
    def update(self, request, pk=None, *args, **kwargs):
        """
        Actualiza la instancia del modelo Familiar especificada.
        
        Args:
            request (Request): La solicitud que contiene los datos para actualizar.
            pk (int): La clave primaria de la instancia del modelo Familiar a actualizar.
        
        Returns:
            Response: Una respuesta HTTP con los datos actualizados o los errores de validación.
        """
        familiar_instance = self.get_queryset(pk)
        if familiar_instance:
            familiar_serializer = self.serializer_class(familiar_instance, data=request.data)
            if familiar_serializer.is_valid():
                familiar_serializer.save()
                return Response(familiar_serializer.data, status=status.HTTP_200_OK)
            return Response(familiar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Objeto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        
class FamiliarDestroyApiView(DestroyAPIView):
    """
    Esta clase proporciona una vista de la API que permite eliminar una instancia específica del modelo Familiar.
    
    Hereda de DestroyAPIView que proporciona la operación DELETE para eliminar un objeto.
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (IsAuthenticated,)
    
    # Define el queryset que se utilizará para obtener los datos del modelo Familiar.
    queryset = Familiar.objects.all()
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo Familiar
    # a y desde representaciones de datos como JSON.
    serializer_class = FamialiarSerializer
 

class PatientCreateListApiView(ListCreateAPIView):
    """
    Esta clase proporciona una vista de la API que permite listar y crear instancias del modelo Patient.
    
    Hereda de ListCreateAPIView que proporciona las operaciones GET (para listar objetos) y POST (para crear un nuevo objeto).
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (IsAuthenticated,)
    
    # Define el queryset que se utilizará para obtener los datos del modelo Patient.
    # Ordena los resultados por el campo 'first_name' y prefetch_related para optimizar las consultas de relaciones.
    queryset = Patient.objects.all().order_by('first_name').prefetch_related()
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo Patient
    # a y desde representaciones de datos como JSON.
    serializer_class = PatientSerializer

    
class PatientRetrieveApiView(RetrieveAPIView):
    """
    Esta clase proporciona una vista de la API que permite recuperar (obtener) una instancia específica del modelo Patient.
    
    Hereda de RetrieveAPIView que proporciona la operación GET para obtener un solo objeto.
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (IsAuthenticated,)
    
    # Define el queryset que se utilizará para obtener los datos del modelo Patient.
    # Se utiliza prefetch_related para optimizar las consultas de relaciones.
    queryset = Patient.objects.all().prefetch_related()
    
    # Define la clase de serializador que se utilizará para convertir la instancia del modelo Patient
    # a y desde representaciones de datos como JSON.
    serializer_class = PatientDetailsSerializer

class PatientUpdateApiView(UpdateAPIView):
    """
    Esta clase proporciona una vista de la API que permite actualizar una instancia específica del modelo Patient.
    
    Hereda de UpdateAPIView que proporciona la operación PUT para actualizar un objeto.
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (IsAuthenticated,)
    
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
    Esta clase proporciona una vista de la API que permite eliminar una instancia específica del modelo Patient.
    
    Hereda de DestroyAPIView que proporciona la operación DELETE para eliminar un objeto.
    """
    
    # Define las clases de permisos que se aplicarán a esta vista.
    permission_classes = (IsAuthenticated,)
    
    # Define el queryset que se utilizará para obtener los datos del modelo Patient.
    queryset = Patient.objects.all()
    
    # Define la clase de serializador que se utilizará para convertir las instancias del modelo Patient
    # a y desde representaciones de datos como JSON.
    serializer_class = PatientSerializer
