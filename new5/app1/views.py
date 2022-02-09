from django.shortcuts import render
from app1.models import student
from app1.forms import studentform
from django.http import HttpResponse
def home(request):

    return render(request,"home.html",{'name':"saranya",'age':21})


def index(request):
    return render(request,"index.html")

def rel(request):
    return render(request,"relative.html")

def studentlist(request):
    k=student.objects.all()
    return render(request,'list.html',{'s':k})

def form1(request):  #First Method
    form=studentform()  # empty form object
    if(request.method=="POST"):
        form=studentform(request.POST)
        if(form.is_valid()):
            form.save()
            return studentlist(request)


    return render(request,'form1.html',{'form':form})

def form2(request):
    if (request.method == "POST"):
        form = studentform(request.POST)
        if (form.is_valid()):
            form.save()
            return studentlist(request)

    return render(request,'form2.html')

def form3(request):
    if (request.method == "POST"):
        n=request.POST['n']
        a=request.POST['a']
        s=student.objects.create(name=n,age=a)
        s.save()
        return studentlist(request)

    return render(request, 'form3.html')

def fact(request):
    if(request.method=="POST"):
        n=int(request.POST['n'])
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return render(request,'fact.html',{'f':fact})

    return render(request,'fact.html')