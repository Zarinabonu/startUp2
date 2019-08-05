from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from register.models import StartUpRegister
from .serializers import RegisterCreateSerializer, RegisterListSerializer
from django.core.mail import EmailMessage, BadHeaderError, send_mail, EmailMultiAlternatives , EmailMessage
from django.core.files.storage import default_storage
from django.conf import settings
# from forms import WorkForm

class RegisterCreate(CreateAPIView):
    queryset = StartUpRegister.objects.all()
    serializer_class = RegisterCreateSerializer

   

    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     settings.EMAIL_HOST_USER,
    #     ['zarinabonu199924@gmail.com'],
    #     fail_silently=True,



    # )
    

class RegisterUpdate(UpdateAPIView):
    queryset = StartUpRegister.objects.all()
    serializer_class = RegisterCreateSerializer
    # lookup_url_kwargs = 'id'

class RegisterDelete(DestroyAPIView):
    queryset =  StartUpRegister.objects.all()
    # lookup_url_kwargs ='id'   
