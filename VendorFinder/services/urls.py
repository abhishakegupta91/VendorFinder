from django.urls import path
from services import views as ser_views

urlpatterns = [
    path('', ser_views.index, name= 'index'),
    path('signup/',ser_views.signup, name='signup'),

]

