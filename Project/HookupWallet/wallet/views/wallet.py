from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import *
from ..serializers import *
from django.conf import settings
# Create your views here.

@api_view(['GET', 'POST','DELETE','PUT'])
def wallet(request):

    if request.method == 'GET':
        id = request.GET.get('wallet_id')
        if id:
            data=Wallet.objects.filter(id=id)
            serializer = WalletSerializer(data)
        else:
            data=Wallet.objects.filter()
            serializer = WalletSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method =='POST':
        serializer = WalletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
