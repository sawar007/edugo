from django.urls import path
from . import views


urlpatterns=[
    path('',views.blogs,name='blogs'),
    path('post/',views.post,name='post'),
    path('post/<int:id>',views.posted, name='posted')

]