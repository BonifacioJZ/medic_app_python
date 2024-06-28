import datetime
from rest_framework import serializers
from .models import Familiar,Patient

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
        return datetime.datetime.now().year - familiar.birth_day.year
    

        
class FamiliarPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ('id','first_name','last_name','curp','email','phone')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id','first_name','last_name','curp','birth_day','familiar')

class PatientDetailsSerializer(serializers.ModelSerializer):
    familiar = FamiliarPatientSerializer(many=True,read_only=True)
    class Meta:
        model = Patient
        fields = ('id','first_name','last_name','curp','email','phone','address','city','colony','birth_day','familiar')
    
    def get_age(self,patient:Patient):
        return datetime.datetime.now().year - patient.birth_day.year  

class PatientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id','first_name','last_name','curp','email','phone','address','city','colony','birth_day','familiar')   
        