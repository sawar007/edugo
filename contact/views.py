from django.shortcuts import render,redirect
from .models import Contact


def sent(request):
    
    if request.method =='POST':
            name = request.POST['name']
            subject = request.POST['subject']
            email = request.POST['email']
            message = request.POST['message']

            data = Contact(name = name, subject=subject,email=email,message=message)
            data.save()
            return redirect('contact')
def contact(request):
   





    return render(request,'contact.html')
