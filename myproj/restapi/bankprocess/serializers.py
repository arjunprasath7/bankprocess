from rest_framework import serializers

from models import User
from models import Transaction

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'address')

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'address','password')

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('id', 'withdrawal', 'deposit','balance','userId',"TransactionDate")

class TransactionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('withdrawal', 'deposit','balance','userId',"TransactionDate")


