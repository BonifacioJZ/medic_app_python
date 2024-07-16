"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import FamiliarCreateListApiView,PatientCreateListApiView,FamiliarRetriveApiView,FamiliarUpdateApiView,FamiliarDestroyApiView
from .views import PatientRetrieveApiView,PatientDestroyApiView,PatientUpdateApiView
urlpatterns = [
    path('',PatientCreateListApiView.as_view(),name="patient_index"),
    path('familiar/',FamiliarCreateListApiView.as_view(),name="familiar_index"),
    path('<str:pk>/',PatientRetrieveApiView.as_view(),name="patient_show"),
    path('<str:pk>/edit/',PatientUpdateApiView.as_view(),name="patient_edit"),
    path('<str:pk>/delete/',PatientDestroyApiView.as_view(),name='patient_destroy'),
    path('familiar/<str:pk>/',FamiliarRetriveApiView.as_view(),name="familiar_show"),
    path('familiar/<str:pk>/edit/',FamiliarUpdateApiView.as_view(),name="familiar_edit"),
    path('familiar/<str:pk>/delete/',FamiliarDestroyApiView.as_view(),name="familiar_destroy"),
]