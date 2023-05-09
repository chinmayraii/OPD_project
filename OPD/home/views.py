from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from . models import *
from django.contrib import auth
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


def index(request):
    return render(request,'registration.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pwd=request.POST['pwd']
        if User.objects.filter(username=uname).exists():
            messages.info(request,"Username already exists")
            return render(request,'registration.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email already exists")
            return render(request,'registration.html')   
        else:
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pwd)
            user.save()
            messages.success(request,"Successfully Registered")
            return render(request,'signin.html')
    else:
        return render(request,'registration.html')

class Opdview():
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated] 
def signin(request):
    if request.method == "POST":
        uname = request.POST['uname']
        upass = request.POST['pwd']
        user = authenticate(username=uname, password=upass)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully !!')
            doctors_name=Doctors_name.objects.all() 
            doc=Doctor.objects.all()
            patients=Patient.objects.all()
            return render(request,'dashboard.html',{'doctors_name':doctors_name,'doc':doc,'patients':patients}) 
        else:
            messages.error(request," Invalid Username or Password")
            return render(request, ("signin.html"))
    else:
        return render(request, ("signin.html"))  

@login_required
def dashboard(request):
    doctors_name=Doctors_name.objects.all() 
    doc=Doctor.objects.all()
    patients=Patient.objects.all()
    return render(request,'dashboard.html',{'doctors_name':doctors_name,'doc':doc,'patients':patients})  

@login_required
def patients(request):
    doctors_name=Doctors_name.objects.all() 
    patients=Patient.objects.all()
    return render(request,'patients.html',{'doctors':doctors_name,'patients':patients})    


def bookappointment(request):
    p=Patient()
    pid=request.POST['doctors']
    p.doctors=Doctors_name.objects.get(id=pid)
    p.patient_name=request.POST['patient_name']
    p.date=request.POST['date']
    p.notes=request.POST['notes']
    p.save()
    messages.success(request," Appointment Booked")
    doctors_name=Doctors_name.objects.all() 
    patients=Patient.objects.all()
    return render(request,'patients.html',{'doctors_name':doctors_name,'patients':patients}) 

@login_required
def doc_dashboard(request):
    doctors_name=Doctors_name.objects.all() 
    doc=Doctor.objects.all()
    patients=Patient.objects.all()
    return render(request,'doc_dashboard.html',{'doctors_name':doctors_name,'doc':doc,'patients':patients})   

def checkup(request):
    d=Doctor()
    pid=request.POST['patient']
    d.patient=Patient.objects.get(id=pid)
    d.medicines=request.POST['medicines']
    d.causes=request.POST['causes']
    d.symptoms=request.POST['symptoms']
    d.file=request.FILES['file']
    d.comments=request.POST['comments']
    d.save()
    messages.success(request," Sucessfully")
    doctors_name=Doctors_name.objects.all() 
    patients=Patient.objects.all()
    doc=Doctor.objects.all() 
    return render(request,'dashboard.html',{'doctors_name':doctors_name,'doc':doc,'patients':patients}) 

def lgout(request):
    auth.logout(request)
    messages.info(request,'sucessfully logout ')
    return redirect('/')                          
