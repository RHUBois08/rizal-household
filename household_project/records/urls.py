from django.urls import path
from .views import hhForm_view, index_view, profiling_view, save_household

app_name = 'records'

urlpatterns = [
    path('', index_view, name='index'),
    path('hh_form/', hhForm_view, name='hh_form'),
    path('profiling/', profiling_view, name='profiling'),
    path('save_household/', save_household, name='save_household'),
]