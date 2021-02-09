from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def hello(request):
    tags = ['น้ำตก','ธรรมชาติ','ลำธาร','หิมะ']
    rating = 4
    return render(request,'tweets/index.html',
    {
        'name':'บทความท่องเที่ยวภาคเหนือ',
        'author':'kong ruksium',
        'tags':tags,
        'rating':rating
    })

def mediumArea(request):
    return render(request,'medium.html')

def registered(request):
    return render(request,'form.html')


def addform(request):
    name=request.POST['nameBlog']
    detail=request.POST['detailBlog']
    return render(request,'result.html',
    {
        'name':name,
        'detail':detail
    })

def tableData(request):
    # Query Data From Model
    data = Post.objects.all()
    return render(request,'table.html',{'post':data})

def register(request):
    return render(request,'register.html')

def addUser(request):
    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['repassword']

    if password==repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username นี้มีคนใช้แล้ว')
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email นี้มีคนใช้แล้ว')
            return redirect('/register')
        else:
            user =  User.objects.create_user(
                username = username,
                first_name = firstname,
                last_name = lastname,
                email = email,
                password = password
            )
            user.save()
            return redirect('/')
    messages.info(request,'รหัสผ่านไม่ตรงกัน')
    return redirect('/register')

def loginForm(request):
    return render(request,'loginForm.html')

def login(request):
    username=request.POST['username']
    password=request.POST['password']
    
    #login
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return redirect('/')
    else :
        messages.info(request,'ไม่พบข้อมูล')
        return redirect('/loginForm')

def logout(request):
    auth.logout(request)
    auth.logout(request)
    return redirect('/')




