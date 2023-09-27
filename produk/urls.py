from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ambil-data-api/', views.ambil_data_api, name='ambil_data_api'),
]
