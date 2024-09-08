from django.urls import path
from . import views

app_name = 'billing'  # Optional: to namespace your URLs in case you have multiple apps

urlpatterns = [
    path('split/evenly/', views.split_evenly, name='split_evenly'),
    path('split/unevenly/', views.split_unevenly, name='split_unevenly'),
    path('split/evenly/tip-tax/', views.split_evenly_include_tip_tax, name='split_evenly_include_tip_tax'),
    path('split/evenly/discount/', views.split_evenly_include_discount, name='split_evenly_include_discount'),
    path('split/shared-items/', views.split_include_shared_items, name='split_include_shared_items'),
]
