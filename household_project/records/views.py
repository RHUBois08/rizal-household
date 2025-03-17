from django.shortcuts import render

def index_view(request):
    return render(request, 'records/index.html')

def hhForm_view(request):
    return render(request, 'records/hh_form.html')

# Create your views here.
