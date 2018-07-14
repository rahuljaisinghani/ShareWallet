from django.shortcuts import render
import uuid
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import *
from ..serializers import *
from django.conf import settings
# Create your views here.

@api_view(['GET', 'POST','DELETE','PUT'])
def add_money(request):
    if request.method == 'PUT':
        id = request.GET.get('user_id')
        money = request.GET.get('personal_amount')
        print(id)
        
        data=User.objects.filter(name=id)
        key=User.objects.get(user_id=str(data[0].user_id))
        wallet_data1=Wallet.objects.filter(wallet_id=str(data[0].wallet_code))
        wallet_data=Wallet.objects.filter(wallet_id=str(data[0].wallet_code)).update(amount=wallet_data1[0].amount+int(money))

        #serializer=UserSerializer(data,data=request.data)
        if data:
            data[0].personal_amount+=int(money)
            #wallet_data[0].amount=70
            #print(wallet_data[0].amount)
            data[0].save()
            print("here")
            instance = Logs()
            instance.wallet=data[0].wallet_code
            instance.user = key
            instance.user_name=data[0].username
            instance.amount_added = int(money)
            instance.description = data[0].name + " Added Rs "+ money + "To the Wallet"
            instance.save()
            #wallet_data[0].save()
            return Response({'update': True},status=status.HTTP_202_ACCEPTED)

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
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST','DELETE','PUT'])
def withdraw_money(request):
    if request.method == 'PUT':
        id = request.GET.get('user_id')
        money = request.GET.get('personal_amount')
        print(id)

        data=User.objects.filter(name=id)
        key=User.objects.get(user_id=str(data[0].user_id))
        wallet_data1=Wallet.objects.filter(wallet_id=str(data[0].wallet_code))
        wallet_data=Wallet.objects.filter(wallet_id=str(data[0].wallet_code)).update(amount=wallet_data1[0].amount-int(money))

        #serializer=UserSerializer(data,data=request.data)
        if data:
            data[0].personal_amount-=int(money)
            #wallet_data[0].amount=70
            #print(wallet_data[0].amount)
            data[0].save()
            print("here")
            #wallet_data[0].save()
            instance = Logs()
            instance.wallet=data[0].wallet_code
            instance.user = key
            instance.user_name=data[0].username
            instance.amount_withdrawn = int(money)
            instance.description = data[0].name + " withdraw rs "+ money + " from the Wallet"
            instance.save()

            return Response({'update': True},status=status.HTTP_202_ACCEPTED)

@api_view(['GET', 'POST','DELETE','PUT'])
def split_bill(request):
    if request.method == 'PUT':
        id = request.GET.get('wallet_id')
        money = request.GET.get('split_bill')
        name=Wallet.objects.filter(wallet_name=id)
        data=User.objects.filter(wallet_code=name[0].wallet_id)
        key=Wallet.objects.get(wallet_id=name[0].wallet_id)
        print(data)
        print(len(data))
        print(int(money)/len(data))
        for each_user in data:
            print(each_user)
            user=User.objects.filter(user_id=str(each_user))
            previous=user[0].group_contribution
            user.update(group_contribution=previous+int(money)/len(data))
        instance = Logs()
        instance.wallet=key
        #instance.user = key
        #instance.user_name=data[0].username
        #instance.amount_withdrawn = int(money)
        instance.description = "Bill of Amount "+ money +" was splited among "+ str(len(data)) + " members of Group"
        instance.save()
        return Response({'update': True},status=status.HTTP_202_ACCEPTED)

