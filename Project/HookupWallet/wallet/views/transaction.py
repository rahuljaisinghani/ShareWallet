from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import *
from ..serializers import *
from django.conf import settings
# Create your views here.

@api_view(['GET', 'POST','DELETE','PUT'])
def transaction(request):
    if request.method == 'GET':
        id = request.GET.get('wallet_id')
        if id:
            data=Logs.objects.filter(id=id)
            serializer = LogsSerializer(data[0])
        else:
            data=Logs.objects.filter()
            serializer = LogsSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
