from django.urls import path
from .views import hhForm_view, index_view, profiling_view

app_name = 'records'

urlpatterns = [
    path('', index_view, name='index'),
    path('hh_form/', hhForm_view, name='hh_form'),
    path('profiling/', profiling_view, name='profiling'),
]