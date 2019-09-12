from django.urls import path
from services import views as ser_views

urlpatterns = [
    path('', ser_views.index),
]
