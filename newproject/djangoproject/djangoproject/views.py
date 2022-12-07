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
import newGadjets
import json

from rest_framework.decorators import api_view
testReqGrapphic = '{"data": [1, 2, 4,5,6]}'

class GadgetApiNewGadgets(APIView):
    #permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ResponseApiNewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if 'folder' not in request.data:
            return Response(['folder'], status=400)
        if 'title' not in request.data:
            return Response(['title'], status=400)
        if 'MAC' not in request.data:
            return Response(['MAC'], status=400)

        #######отправить на сервер данные которые он попытается обработать #########

        return Response({"status": "200"})
class GadgetApiInfo(APIView):
    def post(self, request):
        idSr = request.data['id']
        requestF = Gadjets.objects.get(id=idSr)
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