from rest_framework import serializers
from django.contrib.auth.models import User
from robot.models import TelegramUser,GameStatistic, Referals, Language, Order, Product, Application

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password', 'email']

class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = TelegramUser
        fields =['name','nick_name','balance','chat_id','date_join', 'language', 'spent_balance', 'level', 'make_deposit']


class GameStatisticSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = GameStatistic
        fields =['date','time','player','game_name','bet','win']


class ReferalsSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Referals
        fields =['owner','referal']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Language
        fields = ['func', 'ru', 'en']
       


class OrderSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Order
        fields = ['id','buyer', 'amount', 'currency', 'desc', 'lang', 'status', 'product', 'date', 'time']
        read_only_fields = ('id',)



class ProductSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Product
        fields = ['id','title', 'ru_price', 'usd_price', 'is_active', 'dimes']
        read_only_fields = ('id',)
        
        
class AwalletOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    amount = serializers.IntegerField()
    currency = serializers.CharField(max_length=200)
    test = serializers.BooleanField()
    test_success = serializers.BooleanField()

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Application
        fields = ['id','user', 'amount', 'requisites', 'currency', 'status']
        read_only_fields = ('id',)
