from rest_framework.generics import DestroyAPIView,UpdateAPIView,ListAPIView,CreateAPIView,RetrieveAPIView
from .serializer import ExpedientSerializer,ListExpedietSerializer,CreateExpedientSerializer,ExpedientDetailsSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ExpedientListApiView(ListAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class=ListExpedietSerializer
    queryset=ListExpedietSerializer.Meta.model.objects.all().prefetch_related()
    
class ExpedientCreateApiView(CreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class=CreateExpedientSerializer
    queryset=CreateExpedientSerializer.Meta.model.objects.all()
    
class ExpedientRetrieveViewApiView(RetrieveAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class=ExpedientDetailsSerializer
    queryset=ExpedientDetailsSerializer.Meta.model.objects.select_related().all()

class ExpedientUpdateApiView(UpdateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CreateExpedientSerializer
    queryset = CreateExpedientSerializer.Meta.model.objects.all()

class ExpedientDestroyApiView(DestroyAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class=ExpedientSerializer
    queryset = ExpedientSerializer.Meta.model.objects.all()
    
