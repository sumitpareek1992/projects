from django.shortcuts import render,redirect
from app1.forms import UserRegForm
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def logout_view(request):
	logout(request)
	return redirect("/")
def home_view(request):
	#request.session.set_expiry(10)
	
	
	msg=""
	if request.method=="POST":
		print(dir(request.session))
		data=request.POST
		user=authenticate(username=data["username"],
			password=data["password"])
		if user:
			#import pdb; pdb.set_trace()

		
			print(dir(request.session))
			login(request,user)

			return redirect("/index/")
			msg="Login Succesfully"
		else:
			msg="Login Faild"

	return render(request,"app1/home.html",{"msg":msg})
def user_register(request):
	msg=""
	if request.method=="POST":
		form=UserRegForm(request.POST)
		if form.is_valid():
			form.save()
			user_instance=form.instance
			form.instance.set_password(user_instance.password)
			user_instance.save()

			msg="user register succesfully"
		else:
			msg="data_error"
	form=UserRegForm()
	return render(request,"app1/user_register.html",
		{"form":form,"msg":msg})

                  