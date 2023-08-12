from django.http import HttpResponse
from django.shortcuts import render

from website_app.forms import  Register_form
from website_app.models import Register


# Create your views here.
def firstpage(request):
    return render(request,'frontpage.html')

def home(request):
   return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def courses(request):
    return render(request,'courses.html')

def search(request):
    return render(request,'search.html')

def read(request):
    return render(request,'read.html')

def view(request):
    return render(request,'view.html')

def readmore(request):
    return render(request,'readmore.html')

def register(request):
    l=["c","c++","java","python"]
    if request.method=='POST':
       name=request.POST.get('name')
       mobile=request.POST.get('mobile no')
       email=request.POST.get('email')
       course=request.POST.get('course')
       error_message=None
       print(name,mobile,email,course)
       if(not(name and name.isalpha())):
           error_message='enter name required'

       elif (not (mobile and  len(mobile)==10 and mobile.isdigit())):
           error_message='enter 10 digits number'
       elif (not( email and   email.endswith("@gmail.com"))):
           error_message='enter valid email'
       elif (not (course and course  in l)):
           error_message='enter course required'

       else:

           if not error_message:
             error_message = 'enter valid details'
             r=Register.objects.create(name=name,mobile=mobile,email=email,course=course)
       return render(request,'register.html',{'error':error_message})



    else:
        reg=Register_form()
        return render(request,'register.html',{'form':reg})



