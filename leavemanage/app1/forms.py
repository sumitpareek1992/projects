from django.forms import ModelForm
from app1.models import User , LeaveType



class UserRegForm(ModelForm):
	class Meta:
		model=User
		#fields="__all__"
		fields=["username","password","email","phone","type"]

