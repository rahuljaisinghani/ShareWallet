from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import *
from ..serializers import *
from django.conf import settings
# Create your views here.

@api_view(['GET', 'POST','DELETE','PUT'])
def user(request):

    if request.method == 'GET':
        id = request.GET.get('user_id')
        if id:
            data=User.objects.filter(id=id)
            serializer = UserSerializer(data[0])
        else:
            data=User.objects.all()
            serializer = UserSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method =='POST':
        user=request.data.wallet_code

        wallet_id=Wallet.objects.get(wallet_name=user)
        request.data.wallet_code=wallet_id
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def list_users(request):
    if request.method == 'GET':
        id = request.GET.get('wallet_id')
        data=User.objects.filter(wallet_code=id)
        serializer = UserSerializer(data,many=True)
        print(data)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def login(request):
    username=request.GET.get('username')
    password=request.GET.get('password')
    if username:
        data=User.objects.filter(username=username)
        if password:
            if(data[0].password == password):
                serializer = UserSerializer(data,many=True)
                return Response({'login': True},status=status.HTTP_202_ACCEPTED)
    return Response({'login': False},status=status.HTTP_200_OK)
