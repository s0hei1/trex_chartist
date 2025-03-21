"""
URL configuration for trex_chartist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from trex_chartist.apps.pattern_bank.api.api.dim_symbol_api import DimSymbolAPI
from trex_chartist.apps.pattern_bank.api.api.dim_time import DimTimeApi
from trex_chartist.apps.pattern_bank.api.api.dim_time_frame_api import DimTimeFrameAPI

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Name",
        default_version="v1",
        description="API documentation using Swagger",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('pattern_bank/time', DimTimeApi.as_view()),
    path('pattern_bank/timeframe', DimTimeFrameAPI.as_view()),
    path('pattern_bank/symbol', DimSymbolAPI.as_view()),

]
