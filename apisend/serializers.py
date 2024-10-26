from rest_framework import serializers
from .models import give_data

class getdata(serializers.ModelSerializer):
    class Meta:
        model = give_data        
        fields = ['id','first_name','last_name','phone_number']
        read_only_fields = ['id']
        