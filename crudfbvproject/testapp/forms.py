from testapp.models import Employee,Company
from django import forms
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

   

class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields='__all__'