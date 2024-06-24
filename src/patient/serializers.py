from rest_framework import serializers
from .models import Familiar,Patient

class FamialiarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ('id','first_name','last_name','curp','phone','email')

class PatientListSerializer(serializers.ModelSerializer):
    familiars = FamialiarListSerializer(read_only =True)
    class Meta:
        model = Patient
        fields = ('id','first_name','last_name','curp','phone','email','familiars')
        
        