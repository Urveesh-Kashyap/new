# Create your views here.

from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import get_user_model,authenticate
import json
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
user_mod = get_user_model()
class register(APIView):
    print("hello")
    def post(self,request,format=None):
        data_=json.loads(request.body)
        user_mod=get_user_model()
        uname= data_.get('name')
        password = data_.get('password')
        email = data_.get('email')
        cpassword = data_.get('cpassword')
        all_data = user_mod.objects.all()
        emails = []
        usernames=[]
        for i in all_data:
            emails.append(i.email)
            usernames.append(i.username)
        if password!=cpassword:
            return Response({"status":False,"message":"Password & Confirm Password are not correct"},status=status.HTTP_401_UNAUTHORIZED)
        elif uname in usernames:
            return Response({"status":False,"message":"Username Already Exists"},status=status.HTTP_401_UNAUTHORIZED)
        elif email in emails:
            return Response({"status":False,"message":"Email Already Exists"},status=status.HTTP_401_UNAUTHORIZED)
        elif password==cpassword:
            obj = user_mod(username=uname,password=make_password(password),email=email)
            obj.save()
            return Response({"status":True,'message':'Register successfully'})
class login(APIView):
    def post(self,request,format=None):
        data_=json.loads(request.body)
        user_mod=get_user_model()
        uname= data_.get('name')
        print(uname)
        password = data_.get('password')
        print(password)
        d = authenticate(username=uname,password=password)

        if d is not None:
            return Response({"status":True,"message":"Login Successfully"})
        else:
            return Response({"status":True,"message":"Username & Password is incorrect"})
