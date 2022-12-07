from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from djangoproject.views import GadgetApiNewGadgets, GadgetApiInfo,LoadGraphic
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title="DEMO")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/',schema_view),
    path('GadjetInfo/', GadgetApiInfo.as_view()),
    path('AddGadjet/', GadgetApiNewGadgets.as_view()),
    path('LoadGraphic/', LoadGraphic.as_view()),
    path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   ###
    path('getAccessToken/', TokenRefreshView.as_view(), name='token_refresh'),  ###
    path("logout/", LogoutView.as_view(), name="logout")                        ###
]