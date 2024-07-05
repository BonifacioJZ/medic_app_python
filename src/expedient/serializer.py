from rest_framework import serializers
from .models import Expedient
from src.patient.serializers import PatientExpedientSerializer
from src.user.serializers import UserSerializer


class ExpedientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedient
        fields = ('id','weight','height','pulse','temperature','breathing','systolic','diastolic','patient')
        

class ListExpedietSerializer(serializers.ModelSerializer):
    patient= PatientExpedientSerializer(read_only=True)
    class Meta:
        model = Expedient
        fields = ('id','weight','height','pulse','temperature','breathing','systolic','diastolic','patient')

class CreateExpedientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedient
        fields = ('id','weight','height','pulse','temperature','breathing','systolic','diastolic','patient')

class ExpedientDetailsSerializer(serializers.ModelSerializer):
    patient = PatientExpedientSerializer(read_only=True)
    imc = serializers.SerializerMethodField(method_name="get_imc")
    obesity = serializers.SerializerMethodField(method_name="get_obesity")
    blood_pressure= serializers.SerializerMethodField(method_name="get_blood_pressure")
    user = UserSerializer(read_only=True)
    class Meta:
        model = Expedient
        fields = ('id','weight','imc','obesity','height','pulse','temperature','breathing','systolic','diastolic','blood_pressure','created_at','patient','user')
    
    def get_imc(self,expedient:Expedient)->float:
        return expedient.get_imc()
    
    def get_obesity(self,expedient:Expedient)->str:
        return expedient.get_obesity()
    def get_blood_pressure(self,expedient:Expedient)->str:
        return expedient.get_blood_pressure()
        