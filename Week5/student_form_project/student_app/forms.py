from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(label="Address", widget=forms.Textarea)
    contact_number = forms.CharField(label="Contact Number", max_length=20)
    email_id = forms.EmailField(label="Email ID")
    english_marks = forms.IntegerField(label="English Marks")
    physics_marks = forms.IntegerField(label="Physics Marks")
    chemistry_marks = forms.IntegerField(label="Chemistry Marks")
