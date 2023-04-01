from .models import Customer 
from rest_framework import serializers
from .models import Bapz

class BapzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bapz
        fields = ('productname', 'category','src','price', 'color', 'size','id')


class CustomerSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Customer
        fields = ('email','pwd','id','commands','jwt')