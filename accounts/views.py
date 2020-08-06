from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login


def logout(request):
    if request.method =='POST':
    


        auth.logout(request)
        return redirect('index')

def login(request):
    if request.method =='POST':
        username = request.POST['Username']

        password = request.POST['pass']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return redirect('login')
    else:


        return render(request,'Login.html')

def register(request):
    if request.method =='POST':
        # return render(request,'login')
        username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['pass']
        cpassword = request.POST['cpass']
        if password == cpassword:

            if User.objects.filter(email = email).exists():
                # error
                # print('email')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                # print('username')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username,email = email,password=password)
                user.save()
                return redirect('login')


        else:
            return redirect('register')
    else:
        return render(request,'Register.html')