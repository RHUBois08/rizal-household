from django.shortcuts import render, redirect
from .models import Household

def index_view(request):
    return render(request, 'records/index.html')

def hhForm_view(request):
    return render(request, 'records/hh_form.html')

def profiling_view(request):
    return render(request, 'records/profiling.html')

def save_household(request):
    if request.method == 'POST':
        house_number = request.POST.get('house_number')  # Corrected field name
        household_id = house_number  # Set household_id to house_number
        barangay = request.POST.get('barangay')
        purok = request.POST.get('purok')
        respondent = request.POST.get('respondent')
        philhealth_member = request.POST.get('philhealth_member') == 'yes'
        philhealth_number = request.POST.get('philhealth_number')
        last_names = request.POST.getlist('last_name[]')
        first_names = request.POST.getlist('first_name[]')
        middle_names = request.POST.getlist('middle_name[]')
        suffixes = request.POST.getlist('suffix[]')
        positions = request.POST.getlist('position[]')

 
        try:
            for last_name, first_name, middle_name, suffix, position in zip(last_names, first_names, middle_names, suffixes, positions):
                Household.objects.create(
                    household_id=household_id,
                    barangay=barangay,
                    purok=purok,
                    house_number=house_number,
                    respondent=respondent,
                    philhealth_member=philhealth_member,
                    philhealth_number=philhealth_number,
                    last_name=last_name,
                    first_name=first_name,
                    middle_name=middle_name,
                    suffix=suffix,
                    position=position
                )
            return render(request, 'records/hh_form.html', {'message': 'Data has been saved successfully.'})
        except Exception as e:
            return render(request, 'records/hh_form.html', {'error': str(e)})
    return redirect('records:hh_form')

# Create your views here.
