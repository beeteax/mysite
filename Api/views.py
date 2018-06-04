from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import RemoteInput
from rest_framework.views import APIView
from .serializers import RemoteInputSerializer
import smtplib
from rest_framework.parsers import FileUploadParser
import os
class RemoteApiCall(APIView):
    xyz="1233"
    
    def get(self,request):
        x=RemoteInput()
        x.Address="Hello"
        x.Email="sdncdsn"
        x.FullBath=1
        x.HalfBath=2
        x.Bedrooms=1
        serializer=RemoteInputSerializer(x)
        return Response(serializer.data)


    def post(self, request, format='jpg'):
        #up_file = request.FILES['file']
        x=RemoteInput()
        x.Address="Hello"
        x.Email='up_file.name'
        x.FullBath=1
        x.HalfBath=2
        x.Bedrooms=1
        serializer=RemoteInputSerializer(x)
        return Response(serializer.data)

    def put(self, request,  format=None):
        file_obj = request.FILES['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)
        
       
       # t=threading.Thread(target=ThreadFunction,args=(SA,Unit,HalfBath,FullBath,Bedrooms,Email))
      #  t.start()
        #ThreadFunction(SA,Unit,HalfBath,FullBath,Bedrooms,Email)
        #return render(request, 'personal/predictor.html')
class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, format=None):
        file_obj = request.data['file']
        x=RemoteInput()
        x.Address="Hello"
        x.Email=file_obj.size
        x.FullBath=1
        x.HalfBath=2
        x.Bedrooms=1
        serializer=RemoteInputSerializer(x)
        return Response(serializer.data)
