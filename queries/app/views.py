from django.shortcuts import render,redirect
from . models import *
from django.db.models import Q ,F

def index(request):
    emp=Emp.objects.all()
    data = Emp.objects.get(id=10) 
    data2=Emp.objects.filter(fname="Rashmi")
    data3=Emp.objects.exclude(fname__startswith="R")
    data4=Emp.objects.filter(Q(fname__startswith="S")|Q(lname__startswith="J"))
    data5=Emp.objects.filter(Q(fname__startswith="S")& Q(lname__startswith="J"))
    data6=Emp.objects.filter(fname="raj").values('fname','city','age')
    data7=Emp.objects.annotate(new_age=F('age')*2).values('id','fname','lname','age','new_age')
    data8=Emp.objects.all()[1:6]
    con=Emp.objects.all().count()#cout the number of data in table
    d=Emp.objects.filter(fname__contains="shi")
    j=Emp.objects.filter(age__lt=20)#less then
    k=Emp.objects.filter(age__gte=22)# grater than equal
    return render(request,'index.html',{'state':(STATE_CHOICES),'emp':emp,'e':data,'data2':data2,'data3':data3,
                                        'data4':data4,'data5':data5,'data6':data6,'data7':data7,'data8':data8,
                                        'con':con,'d':d,'j':j,'k':k})


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
    