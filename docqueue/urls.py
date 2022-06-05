"""docqueue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from knox import views as knox_views
from queueing.viewsets.doctor import DoctorViewSet
from queueing.viewsets.patient import PatientViewSet
from queueing.api.auth import SignInAPI, MainUser

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/auth/login', SignInAPI.as_view()),
    path('api/auth/user', MainUser.as_view()),
    path('api/auth/logout',knox_views.LogoutView.as_view(), name="knox-logout"),
    path('admin/', admin.site.urls),
]
