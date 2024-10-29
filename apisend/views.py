from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import getdata
from .models import give_data
from rest_framework import viewsets
from melipayamak import Api
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class send(APIView):
    
    def post(self, request):
        serializer = getdata(data=request.data)
        if serializer.is_valid():

            sender = serializer.save()


            username = '9907911290'
            password = 'Aa@123456'
            api = Api(username, password)
            sms = api.sms()
            to = sender.phone_number
            _from = '50002710011290'
            text = f' سلام جناب {sender.last_name} عزیزوقت بخیر به کافی نت «تاوا پی سی» خوش اومدید برای دریافت آخرین خبرها و ثبت نام ها روی لینک زیر کلیک کنین                             :https://eitaa.com/tavapc_cofeenet'
            response = sms.send(to, _from, text)
            print(response)

            return Response(serializer.data, status=status.HTTP_201_CREATED)  # ایجاد موفق
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # خطای اعتبارسنجی
