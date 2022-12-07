from rest_framework import serializers
from JangoAPI.models import Gusers, Gadjets
from JangoAPI.forms import ResponseGraphic
from rest_framework.serializers import Serializer, CharField

class GusersSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Gusers
        fields = ('userid', 'password')
class GadjetSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Gadjets
        fields = '__all__' ##КИРИЛУ СКЗААТЬ ЧТОБЫ ПОМЕНЯЛ БЛЯСКИЕ ПОЛЯ КЛЮЧИ И ДАТУ НОРМАЛЬНУЮ

class ResponseApiNewSerializer(Serializer):
    folder = CharField()
    title = CharField()
    MAC = CharField()
class ResponseGraphicSerializer(serializers.Serializer):
    graphicview = serializers.CharField()
    items = serializers.CharField()
    type = serializers.CharField()
    range = serializers.IntegerField()
    period = serializers.IntegerField()





