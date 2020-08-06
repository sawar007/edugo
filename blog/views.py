from django.shortcuts import render,redirect, get_object_or_404
from .models import posts


def posted(request,id):

    item = get_object_or_404(posts, pk=id)
    print(item)
    context ={
        'item':item
    }

    return render(request,'blog-single.html',context)


def blogs(request):
    items = posts.objects.all()
    items.order_by('likes')
    context = {
        'items':items
    }


    return render(request,'blog-home.html',context)

def post(request):
    if request.method =='POST':
        title = request.POST['title']
        body = request.POST['body']
        image = request.POST['photo']
        likes = request.POST['likes']
        user_id = request.POST['user_id']
        user_name = request.POST['user_name']
        post_item = posts(title=title,body = body, image=image, likes = likes, user_id = user_id,user_name=user_name)
        post_item.save()
        id = post_item.pk
        return redirect('/blog/post/' + str(id))


    return render(request,'post.html')