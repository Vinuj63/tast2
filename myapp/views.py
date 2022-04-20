from django.shortcuts import render,redirect
from .models import *  
import random
from random import random, randrange
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate
#from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# from django.db import models
# from django.contrib.auth import User
from django.contrib.auth.models import User

# Create your views here.

# @csrf_exempt
# def index(request):
#     return render(request,"index.html")


# @csrf_exempt
# def send_otp(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         print("🚀 ~ file: views.py ~ line 21 ~ email", email)
        
#         otp = random.randint(1000,9999)
        
#         request.session['email'] = email
#         request.session['email_otp'] = otp
        
#         message = f'Your OTP is {otp}'
#         user = User.objects.filter(username=email)
#         print("🚀 ~ file: views.py ~ line 30 ~ user", user)
#         if User.objects.filter(username=email):
#             return redirect('/login/')
#         else:
#             send_mail(
#                 'Email Verification OTP',
#                 message,
#                 settings.EMAIL_HOST_USER,
#                 [email],
#                 fail_silently=False,
#                 )
#             return redirect('/otp/')
        
# @csrf_exempt
# def password(request):
#     if request.method == 'GET':
#         if 'email' in request.session:
#             return render(request, "password.html", {'email':request.session['email']})
#         else:
#             return render(request, "password.html")
    
#     if request.method == 'POST':
#         email = request.session['email']
        
#         u_otp = request.POST['otp']
#         newPassword = request.POST['newPassword']
#         confirmPassword = request.POST['confirmPassword']
#         otp = request.session['email_otp']
        
#         if int(u_otp) == otp:
#             if newPassword == confirmPassword:
#                 if User.objects.filter(username=email):
#                     usr = User.objects.get(username=email)
#                     usr.set_password(newPassword)
#                     usr.save()
#                     return redirect('/login/')
#                 else:
#                     user = User.objects.create_user(username=email, password=newPassword)
#                     user.save()
#                     return redirect('/login/')
#             else:
#                 return redirect('/')
#         else:
#             return redirect('/')


# @csrf_exempt
# def login_request(request):
#     if request.method == 'GET':
#         return render(request, "login.html")
    
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
        
#         user = authenticate(username=email, password=password)
        
#         if user is not None:
#             login(request, user)
#             return render(request, 'login.html', {"msg": "You are now logged in."})
#         else:
#             return render(request, 'login.html', {"msg": "Invalid username or password."})

        
@csrf_exempt
def register(request):
   # return render(request,'index1.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        print("========email=========",email)
        try:
            print("--------------try----------")
            otp = randrange(1000,9999)
            print("--------------otp----------",otp)
            # request.session['email'] = email
            # print("@@@@@@@@@@@@reQUEst###########",request.session['email'])
            # request.session['email_otp'] = otp
            #print("@@@@@@@@@@@@@@@@REQOTP!!!!!!!!!!!!",request.session['email_otp'])
            otpp = CustomUser.objects.create(username=email,email=email,otp=otp)
            print("------otpp------------",otpp)
           # email = request.session['otp']
            subject = 'Welcome to App'
            message = f'Hello {email}!! Your OTP is {otp}'
            print("===========message+++++++++++++",message)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            print("===========recipient=============",recipient_list)
            send_mail(subject, message, email_from, recipient_list)
            # User.objects.create(
            #     email=email,
            #     otp=otp
            # )
            print("++++++++++++++++++++=")
            request.session['email'] = email
            # return render(request,'otp.html')
            return redirect('send-otp')
            
        
            #return render(request,'index3.html')
        except Exception as e:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",e)
            return render(request,'index1.html')
    return render(request,'index1.html')

@csrf_exempt
def send_otp(request):
    print("----------------send_otp-------------")
    email = request.session['email']
    print("----------------email-------------",email)
   # otp = request.session.get['otp']
    if request.method == 'POST':
        id_otp = request.POST.get('otp')
        print('==========id_otp++++++++',id_otp)
        user = CustomUser.objects.filter(email=email).first()
        print("-------------user---------",user)
        New_Password = request.POST.get('newPassword')
        Confirm_Password = request.POST.get('confirmPassword')
        
            
        if id_otp == user.otp and New_Password == Confirm_Password:
            print("-----------upd----------------")
            user.set_password(New_Password)
            user.save()
            msg = 'User Created'
            return render(request,'login.html',{'msg':msg})
        else:
            print("-------------else---------")
            msg = 'Invalid Credentials'
            return render(request,'otp.html', {'msg':msg})
            # return render(request,'login.html')
    return render(request,'otp.html')

@csrf_exempt
def login_request(request):
        
    if request.method == 'POST':
        email = request.POST['email']
        print("--------email----------",email)
        password = request.POST['password']
        print("-----------password------------",password)
        
        user = authenticate(username=email, password=password)
        print("--------201-------",user)
        
        if user is not None:
            login(request, user)
            return render(request, 'dashboard.html', {"msg": "You are now logged in."})
        else:
            return render(request, 'login.html')
    return render(request, "login.html")

@csrf_exempt
def forgot1(request):
    if request.method == 'POST':
        try:
            CustomUser.objects.get(email=request.POST['email'])
            
            otp = randrange(1000,9999)
            
            request.session['otp'] = otp
                           
            email = request.POST['email']
            request.session['email'] = email
            
              
            # otp_f1 = request.POST['otp_f1']
            print("------->>>>>>",otp)
            subject = 'Welcome to App'
            message = f"Hello {request.POST['email']}!! Your OTP is {otp}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'] ]
            send_mail( subject, message, email_from, recipient_list )

            return redirect('forgot2')
    
        except:
            msg = 'Register First'
            return render(request,'index1.html',{'msg':msg})
        
    else:
        return render(request,'forgot1.html')
    
    
@csrf_exempt    
def forgot2(request):
    
    print("-----2111-------")
    otps = request.session['otp']
    print("-=-=-=-=-=-=-=-=-",otps)
    if request.method == 'POST':
        
        uotp = request.POST.get('otp_f1')
        print("==========otp_f1=========",uotp)
        
        if otps != uotp:
            print("==========if===================")
            return redirect('forgot3')
        else:
            print('OTP Not ++++++++++++++++++++++++++++++++++++++++dont Matched')
            return redirect('/')
            # return render(request,'forgot1.html',{'msg':msg,})
        
    else:
        return render(request,'forgot2.html')
        
        
    # if request.method == 'POST':
    #     print("==========213============")
   
    #     uotp = request.POST['otp_f1']
    #     print("==========otp_f1=========",uotp)
        
    #     # if otp == uotp:
    #     #     return render(request,'forgot3.html')
    #     # else:
    #     #     msg = 'OTP Not Matched'
    #     #     return render(request,'forgot1.html',{'msg':msg,})
        
    # else:
        
    #     return render(request,'forgot2.html')
    
def forgot3(request):
    print("=========253===========")
    #user = CustomUser.objects.all()
    #print("=========user===========",user)
    
    # email = request.session['email']
    # print("-=-=-=forgot3-=-=-=-=-=-",email)
    
    if request.method == 'POST':
        print("=========256==========")
        email = request.session['email']
        print("-=-=-=forgot3-=-=-=-=-=-",email)
        newPassword = request.POST['newPassword']
        print("=-=-=-=-=neewPASS-=-=-=-=-=-=",newPassword)
        confirmPassword = request.POST['confirmPassword']
        print("@@@@@@@@@confirm@@@@@@@@@@@",confirmPassword)
        
        if request.POST['newPassword'] == request.POST['confirmPassword']:
            user = CustomUser.objects.get(email=email)
            print("=========user===========",user)
            user.password == request.POST['newPassword']
            user.save   ()
            msg = "PAssword Updated Successfully"
            return render(request,'login.html',{'msg':msg})
    
    
        else:
            msg = 'Password and Confirm_PAssword Not Matched'
            return render(request,'forgot3.html',{'msg':msg}) 
    else:
        return render(request,'forgot3.html')
            
        
        
# @csrf_exempt
# def forgot_password(request):
#     print("---------211--------",211)
    
#     if request.method == "POST":
        
#         # cust = CustomUser.objects.get(email=request.POST['email'])
#         # print("-----------cust-----------",cust)
#         email = request.POST.get("email")
#         print("---------------",email)
        
#         otp = random.randint(1000,9999)
        
#         request.session['email'] = email
#         request.session['email_otp'] = otp
        
#         message = f'your otp is {otp}'
        
#         send_mail(
#             'Email Verification OTP',
#             message,
#             settings.EMAIL_HOST_USER,
#             [email],
#             fail_silently=False,
#         )
#         return redirect('/register/')
#     return render(request,'forgot1.html')


        
        
    
        

        

    
    
    
        
            
            
    