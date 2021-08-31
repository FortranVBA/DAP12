"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from account.views import SignUpView, StaffModelsViewSet
from client.views import ClientModelViewSet
from contract.views import ContractModelViewSet
from event.views import EventModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"users", StaffModelsViewSet, basename="users")
router.register(r"clients", ClientModelViewSet, basename="clients")
router.register(r"contracts", ContractModelViewSet, basename="contracts")
router.register(r"events", EventModelViewSet, basename="events")

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path("login/", TokenObtainPairView.as_view(), name='login'),
    path("login/refresh/", TokenRefreshView.as_view(), name='refresh'),
]

urlpatterns += router.urls
