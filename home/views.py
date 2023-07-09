from django.shortcuts import render,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    context={
        'variable':"this is sent"
        }
    # return HttpResponse("This is homepage")
    return render(request, 'index.html',context)

def about(request):
        return render(request, 'about.html')

def services(request):
        return render(request, 'services.html')

def contacts(request):
        if request.method=="POST":
                name=request.POST.get('name')
                email=request.POST.get('email')
                phone=request.POST.get('phone')
                desc=request.POST.get('desc')
                contacts=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
                contacts.save()
                messages.success(request, 'Your message has been sent!')
        return render(request, 'contacts.html')

def signup(request):
        if request.method=="POST":
                username=request.POST['username']
                email=request.POST['email']
                password=request.POST['password']
                cpassword=request.POST['cpassword']
                myuser=User.objects.create_user(username, email, password)
                myuser.save()
                messages.success(request, 'Account created successfully!')
                
                return redirect('/')
        return render(request, 'signup.html')

def user_login(request):
        if request.method=="POST":
                username=request.POST['username']
                password=request.POST['password']
                
                user =authenticate(username=username, password=password)
                
                if user is not None:
                        login(request, user)
                        messages.success(request, 'Successfully loggedin!')
                        return render(request, 'index.html')
                else:
                
                        messages.danger(request, 'Wrong credientials!')
                        return redirect('/user_login')
                
        return render(request, 'user_login.html')

def user_logout(request):
        logout(request)
        messages.success(request, 'Logged out successfully!')
        return redirect('/')