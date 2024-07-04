import datetime
from rest_framework import serializers
from .models import Familiar,Patient
from src.expedient.models import Expedient
class FamialiarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ('id','first_name','last_name','curp','email','phone','address','city','colony','birth_day')
        

class PatientFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id','first_name','last_name','curp')

class FamiliarDetailsSerializer(serializers.ModelSerializer):
    
    familiar = PatientFamiliarSerializer(many=True,read_only=True)
    age = serializers.SerializerMethodField(method_name='get_age')
    class Meta:
        model = Familiar
        fields= ('id','first_name','last_name','curp','email','phone','address','city','colony','birth_day','age','familiar')
    
    def get_age(self,familiar:Familiar):
        return familiar.get_age()
    

        
class FamiliarPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ('id','first_name','last_name','curp','email','phone')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id','first_name','last_name','curp','birth_day','familiar')

class PatientExpedientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id','first_name','last_name','curp','birth_day')

class ListExpedietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedient
        fields = ('id','weight','height','pulse','temperature','breathing','systolic','diastolic')
        
class PatientDetailsSerializer(serializers.ModelSerializer):
    patient =  serializers.SerializerMethodField(method_name="get_expedients")
    familiar = FamiliarPatientSerializer(many=True,read_only=True)
    class Meta:
        model = Patient
        fields = ('id','first_name','last_name','curp','email','phone','address','city','colony','birth_day','familiar','patient')
    
    def get_age(self,patient:Patient):
        return patient.get_age() 
    
    def get_expedients(self,patient:Patient):
        query = ListExpedietSerializer.Meta.model.objects.filter(patient=patient,is_active=True)
        response= ListExpedietSerializer(query,many=True,read_only=True)
        return response.data 

class PatientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id','first_name','last_name','curp','email','phone','address','city','colony','birth_day','familiar')   
        