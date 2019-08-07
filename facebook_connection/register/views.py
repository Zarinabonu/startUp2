from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
# from register.models import StartUpRegister
from .models import StartUpRegister, User
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import facebook
from rest_framework.authtoken.models import Token
import json


class RegisterListView(ListView):
    # template_name = 'about/list.html'
    model = StartUpRegister
    context_object_name = 'registers'


class RegisterCreateView(TemplateView):
    pass


# template_name = 'about/create.html'
class RegisterUpdateView(DetailView):
    # template_name = 'about/update.html'
    model = StartUpRegister
    context_object_name = 'register'


class LogInView(View):
    def get(self, request):
        print('AAAAAAAAAAAAAA')
        return render(request, 'index.html')

    def post(self, request):
        print('QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print('USERNAME', username, ' PASSWORD', password)
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            print('ERROR')


class LogOut(View):
    def logout(request):
        logout(request)

@csrf_exempt
def login(request):
    print('AAAAAAA',request.POST['token'])
    # return('sasasa')
    # data = json.loads(request.body.decode('utf-8'))
    # new_user = False
    # access_token = data.get('accessToken')
    try:
        graph = facebook.GraphAPI(access_token=request.POST['token'])
        user_info = graph.get_object(
            id='me',
            fields='id')
    except facebook.GraphAPIError:
        return JsonResponse({'error': 'Invalid data'}, safe=False)

    try:
        user = User.objects.get(facebook_id=user_info.get('id'))

    except User.DoesNotExist:
        password = User.objects.make_random_password()
        user = User(
            email=user_info.get('email')
            or '{0} without email'.format(user_info.get('last_name')),
            username='username'

        )
        user.set_password(password)
        user.save()
        new_user = True
    token = Token.objects.get(user=user).key
    if token:
        return JsonResponse({'auth_token': token, 'new_user': new_user},
                           safe=False)
    else:
        return JsonResponse({'error':'Invalid data'}, safe=False)


class face_login(TemplateView):
    template_name = 'test.html'

