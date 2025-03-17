from django.shortcuts import render

def index_view(request):
    return render(request, 'reports/index.html')

# Create your views here.
