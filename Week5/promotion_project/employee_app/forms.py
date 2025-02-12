from django import forms
from datetime import date

class EmployeeForm(forms.Form):
    employee_id = forms.ChoiceField(label="Employee ID", choices=[('EMP001', 'EMP001'), ('EMP002', 'EMP002'), ('EMP003', 'EMP003')])
    date_of_joining = forms.DateField(
        label="Date of Joining",
        widget=forms.DateInput(attrs={'type': 'date'}),  # Use HTML5 date input
    )

    def clean_date_of_joining(self):
        date_of_joining = self.cleaned_data['date_of_joining']
        if date_of_joining > date.today():
            raise forms.ValidationError("Date of Joining cannot be in the future.")
        return date_of_joining
 