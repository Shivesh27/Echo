from django.shortcuts import render
from .forms import UserRegisterForm
# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f'Account created! You can login now!')
			return redirect('#')
	else:	
		form = UserRegisterForm()
	return render(request,'register.html',{'form': form})