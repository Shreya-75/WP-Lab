from django.shortcuts import render
from .forms import EmployeeForm
from datetime import date

def check_eligibility(request):
    eligibility = None  # Initialize eligibility outside the if block

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            date_of_joining = form.cleaned_data['date_of_joining']
            today = date.today()
            experience_years = today.year - date_of_joining.year - (
                (today.month, today.day) < (date_of_joining.month, date_of_joining.day)
            )

            eligibility = experience_years >= 5  # Determine eligibility

    else:
        form = EmployeeForm()  # Create an unbound form for the initial display

    return render(
        request,
        'employee_app/employee_form.html',
        {'form': form, 'eligibility': eligibility},  # Pass form and eligibility to the template
    )
