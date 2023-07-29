from django.shortcuts import render  , redirect
from .models import Blog , BlogComment
from datetime import datetime
from distutils.command.upload import upload
from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User 
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request , 'home.html' , {'blogs':blogs})

def blog(request ,slug):
    post = Blog.objects.filter(s_no=slug).first()
    comments = BlogComment.objects.filter(post=post)
    print(request.user)
    context= {'info':post,'comments':comments , 'user':request.user}
    return render(request, 'blog.html' , context)

def postComment(request):
    if request.method=='POST':
        comment= request.POST.get('comment')
        user=request.user
        postSno=request.POST.get('postSno')
        post=Blog.objects.get(s_no=postSno)


        comment=BlogComment(comment=comment,user=user,post=post)
        comment.save()
        messages.success(request , 'Your Comment has been posted Succesfully')
    return redirect(f"/blog/{post.s_no}")

def auth_login(request):
    if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["pass"]
            user = authenticate(username= email , password= password)
            if user is not None and user.is_active:
                login(request , user)
                return redirect("home")
            elif request.user.is_authenticated:
                return redirect('home')
            else:
                message = messages.error(request , "Incorrect credentials provided")
                return redirect("home")
    else:
        return render(request , 'login.html')

def signup(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            username_user = request.POST['name']
            email_user = request.POST.get('email_user')
            password_user = request.POST['pass_user']

            user = User.objects.create_user(username_user , email_user , password_user)
            user.save()

            messages.success(request , 'Successfully Signed In')
            return redirect('home')
        
        else:
            return render(request , "signup.html")
    else:
        return redirect('home')
    
def logout_user(request):
    logout(request)
    return redirect('home')

def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            u_name = request.POST.get('u_name')
            u_title = request.POST.get('u_title')
            descp = request.POST.get('descp')
            video = request.FILES['photo']
            date = request.POST.get('date')

            upload = Blog(b_name=u_title ,b_descp=descp, b_photo = video , b_author=u_name , b_date=date)
            upload.save()

            messages.success(request , "Successfully uploaded the Blog !")
            return redirect('create')

        Uploads = Blog.objects.all()
        return render(request , "create.html" , {'upload':Uploads})
    else :
        return redirect("home")

def search(request):
    if request.method == 'GET':
            query = request.GET.get('query')
            search_for_title = Blog.objects.filter(b_name__icontains=query)
            search_for_author = Blog.objects.filter(b_author__icontains=query)

            if search_for_author:
                result = search_for_author
            elif search_for_title:
                result = search_for_title
            else:
                result="No Results Found"
                

            return render(request , "search.html" , {'query':query , 'result':result , 's_for_title':search_for_title , 's_for_author':search_for_author})
    return HttpResponse('Please Search for something ... ')
    
    

 