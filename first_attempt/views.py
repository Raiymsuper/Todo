from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import RetrieveUpdateAPIView, GenericAPIView
from rest_framework.response import Response

from .models import Todo, AvbMoney
from .serializers import TodoSerializer, AvbMoneySerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



class AvbMoneyDetailView(GenericAPIView):
    queryset = AvbMoney.objects.all()
    serializer_class = AvbMoneySerializer

    # GET method (Retrieve)
    def get(self, request, pk, *args, **kwargs):
        try:
            money = self.get_object()
            serializer = self.get_serializer(money)
            return Response(serializer.data)
        except AvbMoney.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    # PUT method (Update)
    def put(self, request, pk, *args, **kwargs):
        money = self.get_object()
        serializer = self.get_serializer(money, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)