from django.shortcuts import render
from django.urls import include, re_path
from rest_framework_swagger.views import get_swagger_view
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from djangoproject.serializer import  GadjetSerialazer, ResponseGraphicSerializer, ResponseApiNewSerializer
from rest_framework import generics, viewsets, request, status
from .models import Gusers, Gadjets
from djangoproject import newGadjets
import json

class AddNewGadget(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ResponseApiNewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        #######отправить на сервер данные которые он попытается обработать #########

        return Response(status=200)
class LoadGadgetApiInfo(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        idSr = request.data['id']
        requestF = Gadgets.objects.get(id=idSr)
        return Response(GadjetSerialazer(requestF, many=False).data)
class AutenficationAPI(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
class LoadGraphic(APIView):
    def post(self, request):
        serializer =  ResponseGraphicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        requestJ=json.dumps(request.data)
        #####- отправить данные в ввисде массива и отправить данные и присвоить значение тут
        return Response({"status": "200"})
class LoadGadgetFolder(APIView):
    permission_classes = [IsAuthenticated]
    def get (self, request):
        idSr = request.data['id']
        requestF = Gadgets.objects.filter(folder=idSr).order_by('device_type')
        return Response(GadjetFolderSerialazer(requestF, many=True).data)
class LoadUploadingApiInfo(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        idSr = request.data['id']
        requestF = Uploading.objects.get(id=idSr)
        return Response(UploadingSerialazer(requestF, many=False).data)
class LoadUploadingFolder(APIView):
    permission_classes = [IsAuthenticated]
    def get (self, request):
        idSr = request.data['id']
        requestF = Uploading.objects.filter(folder=idSr).order_by('device_type')
        return Response(GadjetFolderSerialazer(requestF, many=True).data)
class AddNewUploanding(APIView):
    permission_classes = [IsAuthenticated]
    def post (self,request):
        serializer = ResponseApiNewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Uploading.objects.create(folder = request.data['folder'],
        title = request.data['title'],
        type_values = request.data['type_values'],
        devices_in_unloading = request.data['devices_in_unloading'],
        type_of_unloading = request.data['type_of_unloading'],
        range = request.data['range'],
        period = request.data['period'],id =id.uuid4())
        return Response(status=200)