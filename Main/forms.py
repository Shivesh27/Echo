from django import forms
from .models import PendingUsers

class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = PendingUsers
		fields = ['name', 'email', 'gender', 'collegeid', 'enrollmentnumber', 'yearofjoin', 'contact','idproof']
	