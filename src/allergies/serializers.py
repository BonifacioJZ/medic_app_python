from rest_framework import serializers
from .models import Allergies
from src.patient.models import Patient


class PatientAllergiesSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name="get_full_name")
    class Meta:
        model = Patient
        fields =('id','full_name','curp')
    
    def get_full_name(self,patient:Patient)->str:
        return f'{patient.first_name} {patient.last_name}'
        

class AllergiesListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Allergies
        fields = ('id','name','description','slug',)
        
class AllergiesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergies
        fields = ('id','name','description',)

class AllergiesReatriveSerializer(serializers.ModelSerializer):
    allergies = PatientAllergiesSerializer(read_only=True,many=True)
    class Meta:
        model = Allergies
        fields =('id','name','description','allergies','slug',)