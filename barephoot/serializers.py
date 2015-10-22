from rest_framework import serializers
from barephoot.models import Movdata
from barephoot.models import Restdata
from barephoot.models import TheatreDetail
from barephoot.models import PlacestoVisit
from barephoot.models import Events
from django.contrib.auth.models import User


class Nserializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Movdata
        fields = ('movie_name','theatre','timing','owner')


class MDserializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreDetail
        fields = ('theatre','lat','long','rating','price2')

class Rserializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Restdata
        fields = ('name','lat','long','rating','price2','owner')

class UserSerializer(serializers.ModelSerializer):
    barephoot = serializers.PrimaryKeyRelatedField(many=True,queryset=Movdata.objects.all())
    class Meta:
        model = User
        fields = ('id','username','barephoot')

class PlaceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = PlacestoVisit
        fields = ('name','address','category','timings','rating','review_count','owner')


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Events
        fields = ('name','address','day','time','owner')