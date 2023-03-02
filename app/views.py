from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Create your views here.

class UserModelView(APIView):
    def get(self, request):
         try:
             data = User.objects.all()
             serializer = UserSerializer(data, many=True)
             
             return Response(serializer.data)
                
         except Exception as e:
             return Response(status=status.HTTP_404_NOT_FOUND)
         

class UserModelView1(APIView):
    def get(self, request, pk):
         try:
             data = User.objects.get(id=pk)
             serializer = UserSerializer(data)
             
             return Response(serializer.data)
                
         except Exception as e:
             return Response(status=status.HTTP_404_NOT_FOUND)
         
         
         
@receiver(pre_save, sender=User)    
def task(sender , instance, **kwargs):
    print("fetched____________________________________________________________________________________________")
    
    if User:
        obj=User.objects.all()
        print(obj)  
        