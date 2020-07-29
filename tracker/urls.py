from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('<country>', views.covid, name='covid'),
]