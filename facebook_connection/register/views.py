from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from register.models import StartUpRegister


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
    def get(self,request):
        print('AAAAAAAAAAAAAA')
        return render(request,'index_login.html')

    def post(self, request):
        print('QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('banner-list')
        else  :
            print('ERROR')