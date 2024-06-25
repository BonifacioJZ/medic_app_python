from rest_framework import serializers
from .models import Familiar,Patient

class FamialiarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ('id','first_name','last_name','curp','email')
        
class CreateFamiliarSerializer(serializers.ModelSerializer):
    
    
    #age = serializers.SerializerMethodField(method_name="get_age")
    class Meta:
        model = Familiar
        fields = ('id','first_name','last_name','curp','email','address','city','colony','birth_day')
    
    def get_age(self,familiar:Familiar)->int:
        return familiar.get_age
    
    
class PatientListSerializer(serializers.ModelSerializer):
    familiars = FamialiarListSerializer(read_only =True)
    class Meta:
        model = Patient
        fields = ('id','first_name','last_name','curp','email','familiars')
        
        