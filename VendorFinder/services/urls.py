from django.urls import path
from services import views as ser_views

urlpatterns = [
    path('', ser_views.index),
    path('customer-profile', ser_views.cutomer_profile),
    path('vendor-profile', ser_views.vendor_profile),
    path('request-page', ser_views.vendor_customer_request_page),
    path('vendor-filter', ser_views.vendor_filter_page),

]
