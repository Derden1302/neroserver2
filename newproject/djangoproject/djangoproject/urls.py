from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from djangoproject.views import AddNewGadget, LoadGadgetApiInfo,LoadGraphic,LoadGadgetFolder, LoadUploadingFolder,LoadUploadingApiInfo
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title="DEMO")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/',schema_view),

    path('gadget/GadjetInfo/', LoadGadgetApiInfo.as_view()),
    path('gadget/AddGadjet/', AddNewGadget.as_view()),
    path('gadget/GadgetFolder/', LoadGadgetFolder.as_view()),

    path('uploading/LoadGraphic/', LoadGraphic.as_view()),
    path('uploading/AddNewUploading/', LoadGraphic.as_view()),
    path('uploading/UploadingFolder/', LoadUploadingFolder.as_view()),
    path('uploading/UploadingInfo/', LoadUploadingApiInfo.as_view()),

    path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   ###
    path('getAccessToken/', TokenRefreshView.as_view(), name='token_refresh'),  ###
    path("logout/", LogoutView.as_view(), name="logout")

]