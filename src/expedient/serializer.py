from rest_framework import serializers
from .models import Expedient
from src.patient.serializers import PatientExpedientSerializer


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
    class Meta:
        model = Expedient
        fields = ('id','weight','height','pulse','temperature','breathing','systolic','diastolic','created_at','patient')
        
        