from rest_framework import serializers
from .models import Allergies


class AllergiesListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Allergies
        fields = ('id','name','description','slug',)
        
class AllergiesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergies
        fields = ('id','name','description',)

class AllergiesReatriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergies
        fields =('id','name','description','slug',)