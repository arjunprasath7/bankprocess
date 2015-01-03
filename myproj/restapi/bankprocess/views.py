from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import User,Transaction
from bankprocess.serializers import UserSerializer,TransactionSerializer,UserCreateSerializer,TransactionCreateSerializer


@api_view(['GET', 'POST','PUT','DELETE'])
def user_details(request,username,password):
    """
    list customer details 
    """
    # customer = User.objects.get(username=username,password=password)
    if request.method == 'POST':
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    try:
        
        customer = User.objects.get(username=username,password=password)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(customer)
        return Response(serializer.data)

    elif request.method == 'PUT':
    	serializer = UserSerializer(customer, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST','PUT'])
def list_transaction(request,pk):
    # transaction_list = Transaction.objects.filter(userId=pk)
    try:
        transaction_list = Transaction.objects.filter(userId=pk)
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TransactionSerializer(transaction_list,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TransactionCreateSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

