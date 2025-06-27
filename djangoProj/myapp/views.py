from django.shortcuts import render, redirect
from .forms import TeacherForm
from .models import Teacher
from .import views

def index(request):
    return render(request, 'index.html')

def insert_teacher(request):
   
   fname= request.POST['fname']
   lname= request.POST['lname']
   email= request.POST['email']

   newuser=Teacher.objects.create(
       first_name=fname,
       last_name=lname,
       email=email,

    )
   return redirect('showpage')

def show_page(request):
    all_data=Teacher.objects.all()
    return render(request,'show.html',{'key1':all_data})

def EditPage(request, pk):
    get_data= Teacher.objects.get(id=pk)
    return render(request,"edit.html",{'key2':get_data})


def updateData(request,pk):
    udata=Teacher.objects.get(id=pk)
    udata.first_name=request.POST['fname']
    udata.last_name=request.POST['lname']
    udata.email=request.POST['email']
    udata.save()
    return redirect('showpage')

def deletedata(request, pk):
    deletedata=Teacher.objects.get(id=pk)
    deletedata.delete()
    return redirect('showpage')
