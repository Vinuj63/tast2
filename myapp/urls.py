from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.register,name='register'),
  #  path('index3/',views.index3,name='index3'),
    # path('otp/',views.otp,name='otp'),
    path('send-otp/', views.send_otp, name='send-otp'),
    path('login/',views.login_request,name='login'),
    #path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('forgot1/',views.forgot1, name='forgot1'),
    path('forgot2/',views.forgot2,name='forgot2'),
    path('forgot3/',views.forgot3,name='forgot3'),
]