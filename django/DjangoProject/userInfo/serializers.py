from rest_framework import serializers
from .models import *

class userInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'