import datetime as datetime
from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import  GadjetSerialazer, ResponseGraphicSerializer, ResponseApiNewSerializer, GadjetFolderSerialazer, UploadingSerialazer, UploadingFolderSerialazer
from .models import Gusers, Gadgets, Uploading, Indata
import uuid as id
from datetime import datetime, timedelta
class AddNewGadget(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        Gadgets.objects.create(title=request.data['title'],
                                 folder=request.data['folder'],
                                 mac = request.data['MAC'],
                                 device_type=request.data['device_type'],
                               id=id.uuid4())
        return Response(status=200)
class LoadGadgetApiInfo(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        idSr = request.GET.get('id')
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
periodD = { 1 : 60, 2 : 30, 3:1440}
rangeD={24 : 1 ,3 : 3,7 : 7}
class LoadLineGraphic(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer =  ResponseGraphicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        graphicview = request.data['graphicview']
        items = request.data['items']
        type = request.data['type']
        range_date = rangeD[request.data['range']]
        period = periodD[request.data['period']]
        start_date = datetime.today() - timedelta(days=range_date)
        end_date = datetime.today()
        ResponseGrafic=[]
        WATTarrA, WATTarrV=[], []
        requestP = Indata.objects.filter( time_zone__range=[start_date, end_date])
        for i in range(0, (end_date-start_date).days*1440, period ):
            end_date =  start_date + timedelta(minutes=period)
            requestC = requestP.filter(time_zone__range=[start_date, end_date])
            if type == 'AMPER':
                start_date = end_date
                ResponseGrafic.extend((requestC.aggregate(Avg('amperage')).values()))

            elif type == 'VOLTAGE':
                start_date = end_date
                ResponseGrafic.extend((requestC.aggregate(Avg('voltage')).values()))
            elif type == 'WATT':
                start_date = end_date

                WATTarrA.extend((requestC.aggregate(Avg('amperage')).values()))
                WATTarrV.extend((requestC.aggregate(Avg('voltage')).values()))
                #ResponseGrafic = a*b
        if type == 'WATT':
            for i in range(0,len( WATTarrV)):
                if WATTarrV[i]!=None or WATTarrA[i]!=None:
                    ResponseGrafic.append(WATTarrV[i]*WATTarrA[i])

        return Response(ResponseGrafic)
    def serrialize(self, title):

        return
class LoadGadgetFolder(APIView):
    permission_classes = [IsAuthenticated]
    def get (self, request):
        idSr = request.GET.get('id')
        requestF = Gadgets.objects.filter(folder=idSr).order_by('device_type')
        return Response(GadjetFolderSerialazer(requestF, many=True).data)
class LoadUploadingApiInfo(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        idSr = request.data.get('id')
        requestF = Uploading.objects.get(id=idSr)
        return Response(UploadingSerialazer(requestF, many=False).data)
class LoadUploadingFolder(APIView):
    permission_classes = [IsAuthenticated]
    def get (self, request):
        idSr = request.GET.get('id')
        requestF = Uploading.objects.filter(folder=idSr).order_by('type')
        return Response(UploadingFolderSerialazer(requestF, many=True).data)
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

