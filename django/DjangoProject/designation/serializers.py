from rest_framework import serializers
from .models import *

class designationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'