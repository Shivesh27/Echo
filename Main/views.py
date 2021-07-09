from django.shortcuts import render
from django.contrib.auth import login , logout
from .LoginBackend import LoginBackend
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request,"index.html")


def login_page(request):
    return render(request,"login.html")



def admin_dash(request):
    return render(request,"admin_dash.html")

def teacher_dash(request):
    return render(request,"teacher_dash.html")

def student_dash(request):
    return render(request,"student_dash.html")


def login_val(request):
    if request.method != "POST":
        return HttpResponse("<h2>Error</h2>")
    else:
        user = LoginBackend.authenticate(request,request.POST.get("email"),request.POST.get("password"))
    if user != None:
        login(request,user)
        if user.user_type== '1':
            return HttpResponseRedirect('/admin_home')
        elif user.user_type == '2':
            return HttpResponseRedirect('/teach_home')
        else:
            return HttpResponseRedirect('/stu_home')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")