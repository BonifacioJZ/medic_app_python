from rest_framework import serializers
from .models import Expedient


class ExpedietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedient
        fields = ('id','weight','height','pulse','temperature','breathing','systolic','diastolic','patient')