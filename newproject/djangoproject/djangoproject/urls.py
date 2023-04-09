from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import AddNewGadget, LoadGadgetApiInfo,LoadLineGraphic,LoadGadgetFolder, LoadUploadingFolder,LoadUploadingApiInfo, AddNewUploanding, GadgetActiveChecker, AddNewDataFromHub
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title="DEMO")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/',schema_view),

    path('gadget/GadgetInfo/', LoadGadgetApiInfo.as_view()), #get
    path('gadget/AddGadjet/', AddNewGadget.as_view()),
    path('gadget/GadgetFolder/', LoadGadgetFolder.as_view()), #get
    path('gadget/IsActive', GadgetActiveChecker.as_view()), #get активен ли гаджет

    path('uploading/LoadGraphic/', LoadLineGraphic.as_view()),
    path('uploading/AddNewUploading/', AddNewUploanding.as_view()),
    path('uploading/UploadingFolder/', LoadUploadingFolder.as_view()), #get
    path('uploading/UploadingInfo/', LoadUploadingApiInfo.as_view()), #get

    path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   ###
    path('getAccessToken/', TokenRefreshView.as_view(), name='token_refresh'),  ###
    path("logout/", LogoutView.as_view(), name="logout"),
    path('getIndataFromHub/', AddNewDataFromHub.as_view())
]
