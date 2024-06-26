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
    
    familiars = PatientFamiliarSerializer(many=True,read_only=True)
    
    class Meta:
        model = Familiar
        fields= ('id','first_name','last_name','curp','email','phone','address','city','colony','birth_day','familiars')
    

        
class PatientFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ('id','first_name','last_name','curp','email','phone')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id','first_name','last_name','curp','birth_day','familiar')

class PatientDetailsSerializer(serializers.ModelSerializer):
    familiars = PatientFamiliarSerializer(many=True,read_only=True)
    class Meta:
        model = Patient
        fields = ('id','first_name','last_name','curp','email','phone','address','city','colony','birth_day','familiars')  
        