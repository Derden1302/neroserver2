from rest_framework import serializers
from djangoproject.models import Gusers, Gadgets, Uploading, Indata
from djangoproject.forms import ResponseGraphic
from rest_framework.serializers import Serializer, CharField

import uuid as id


class GusersSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Gusers
        fields = ('userid', 'password')


class GraphicSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Indata
        fields = '__all__'


class GadjetSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Gadgets
        fields = '__all__'

class GadjetActiveSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Gadgets
        fields = ('id','status')

class GadjetFolderSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Gadgets
        fields = ('id', 'title', 'device_type')


class ResponseApiNewSerializer(Serializer):
    folder = serializers.UUIDField()
    title = CharField()
    MAC = CharField()
    device_type = CharField()


class AddNewUploanding(Serializer):
    folder = serializers.UUIDField()
    title = CharField()
    type_values = CharField()
    devices_in_unloading = CharField()
    type_of_unloading = CharField()
    range = serializers.IntegerField()
    period = serializers.IntegerField()


class ResponseGraphicSerializer(serializers.Serializer):
    graphicview = serializers.CharField()
    items = serializers.CharField()
    type = serializers.CharField()
    range = serializers.IntegerField()
    period = serializers.IntegerField()


class UploadingSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Uploading
        fields = '__all__'


class UploadingFolderSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Uploading
        fields = ('id', 'title', 'type')




