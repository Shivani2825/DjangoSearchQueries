from django.shortcuts import render,redirect
from . models import *

def index(request):
    emp=Emp.objects.all()
    data = Emp.objects.get(id=10) 
    data2=Emp.objects.filter(fname="Rashmi")
    data3=Emp.objects.exclude(fname__startswith="R")
    return render(request,'index.html',{'state':(STATE_CHOICES),'emp':emp,'e':data,'data2':data2,'data3':data3})


def adduser(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        age=request.POST['age']
        state=request.POST['state']
        city=request.POST['city']
        zip=request.POST['zip']
        data=Emp.objects.create(fname=fname,lname=lname,state=state,city=city,zip=zip,age=age)
        data.save()
        emp=Emp.objects.all()
        return redirect('/',{'state':(STATE_CHOICES),'emp':emp})
    