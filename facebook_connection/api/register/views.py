from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
# from register.models import StartUpRegister
from .serializers import RegisterCreateSerializer, UserSerializer, RegisterListSerializer
from django.core.mail import EmailMessage, BadHeaderError, send_mail, EmailMultiAlternatives , EmailMessage
from django.core.files.storage import default_storage
from django.conf import settings
# from forms import WorkForm
from register.models import User

class RegisterCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.AllowAny]

    # @method_decorator(ensure_csrf_cookie)
    # @method_decorator(csrf_protect)
    # def create(self, request):
    #     serializer = UserSerializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)

    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     settings.EMAIL_HOST_USER,
    #     ['zarinabonu199924@gmail.com'],
    #     fail_silently=True,



    # )
    

class RegisterUpdate(UpdateAPIView):
    pass
    # queryset = StartUpRegister.objects.all()
    # serializer_class = RegisterCreateSerializer
    # # lookup_url_kwargs = 'id'

class RegisterDelete(DestroyAPIView):
    pass
    # queryset =  StartUpRegister.objects.all()
    # # lookup_url_kwargs ='id'
