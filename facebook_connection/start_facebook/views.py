from django.shortcuts import render
from django.contrib.auth.decorators import login_required

    # Create your views here.
def login(request):
  return render(request, 'start_facebook/login.html')


def home(request):
  return render(request, 'start_facebook/home.html')

# Create your views here.
