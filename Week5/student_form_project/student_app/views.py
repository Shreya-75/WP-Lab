from django.shortcuts import render
from .forms import StudentForm

def student_details(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            date_of_birth = form.cleaned_data['date_of_birth']
            address = form.cleaned_data['address']
            contact_number = form.cleaned_data['contact_number']
            email_id = form.cleaned_data['email_id']
            english_marks = form.cleaned_data['english_marks']
            physics_marks = form.cleaned_data['physics_marks']
            chemistry_marks = form.cleaned_data['chemistry_marks']

            total_marks = english_marks + physics_marks + chemistry_marks
            percentage = (total_marks / 300) * 100

            student_data = f"Name: {name}\nDate of Birth: {date_of_birth}\nAddress: {address}\nContact Number: {contact_number}\nEmail ID: {email_id}\nEnglish Marks: {english_marks}\nPhysics Marks: {physics_marks}\nChemistry Marks: {chemistry_marks}\n"

            return render(request, 'student_app/student_form.html', {'form': form, 'student_data': student_data, 'percentage': percentage})
    else:
        form = StudentForm()
    return render(request, 'student_app/student_form.html', {'form': form})
