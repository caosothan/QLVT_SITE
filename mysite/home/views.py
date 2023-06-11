from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages


#Hàm tạo trang chủ
def createHomepage(request):
   return render(request, "templates/homepage.html", context = {"link_home": "/home/" , "link_contact": "/contact/", "link_login": "/login/", "link_sign_up": "/register/", "link_admin": "/admin/"})


#Hàm tạo form đăng kí
def register(request):
    if request.method == "POST":
        name = request.POST['name']
        gender = request.POST['gender']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # kiểm tra logic đăng kí
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username already existed!")
                return redirect("/register/")
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email already existed!")
                return redirect("/register/")
            else:
                user = User.objects.create_user(username = username, password = password, email = email)
                user.save()
                return redirect("/login/")  
        else:
            messages.info(request, "Confirm password not maching password!")
            return redirect("/register/")
    else:
        return render(request, "templates/register_form.html")






# Hàm tạo form đăng nhập
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Kiểm tra logic đăng nhập
        user = authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("/action/")
        else:
            messages.info(request, "Your username or password not match!")
            return redirect("/login/")

    else:
       
        return render(request, "templates/login_form.html")
            


# Hàm đăng xuất tài khoản
def logout(request):
    auth.logout(request)
    return redirect("/")


# Hàm tạo  trang thông tin liên hệ
def contact(request):
    return render(request, "templates/contact.html", context = {"link_home": "/home/" , "link_contact": "/contact/" ,"link_login": "/login/", "link_sign_up": "/register/", "link_admin": "/admin/"})




