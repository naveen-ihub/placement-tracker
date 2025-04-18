from django.urls import path
from . import views

urlpatterns = [
    path('', views.health_check, name='health_check'),
    path('get_data/', views.get_data, name='get_data'),
    path('add_data/', views.add_data, name='add_data'),
]
