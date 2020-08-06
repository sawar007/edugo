from django.shortcuts import render

def course(request,id):

    if id == 'development':
        from . import web
        res= web.scrap()

        context = {

            'item': res
            
        }

        
        return render(request,'course.html',context)







def courses(request):

    return render(request,'courses.html')