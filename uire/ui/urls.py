from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate', views.generate, name='generate'),
    path('download', views.download, name='download'),
    path('download/<str:cluster_name>', views.download_xul, name='download_xul'),

]