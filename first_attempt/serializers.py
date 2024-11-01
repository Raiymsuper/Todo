from rest_framework import serializers
from .models import Todo, AvbMoney


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class AvbMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = AvbMoney
        fields = ['id', 'amount']