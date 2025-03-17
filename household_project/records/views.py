from django.shortcuts import render

def index_view(request):
    return render(request, 'records/index.html')

def hhForm_view(request):
    return render(request, 'records/hh_form.html')

def profiling_view(request):
    return render(request, 'records/profiling.html')

# Create your views here.
