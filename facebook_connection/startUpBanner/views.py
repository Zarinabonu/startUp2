from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from startUpBanner.models import StartUpBanner


class BannerListView(ListView):
    template_name = 'index.html'
    model = StartUpBanner
    context_object_name = 'banners'

    def get_queryset(self):
    	# print(StartUpBanner.objects.order_by('-data')[:3])
    	u = StartUpBanner.objects.all().order_by('-data')[:3]
    	print(u)
    	return StartUpBanner.objects.all().order_by('-data')[:3]

class BannerAllListView(ListView):
    template_name = 'blog.html'
    model = StartUpBanner
    context_object_name = 'allbanners'

class BannerCreateView(TemplateView):
    template_name = 'contact.html'

class BannerDetatilView(DetailView):
    template_name = 'singlepage.html'
    model = StartUpBanner
    context_object_name = 'singlepost'

class BannerUpdateView(DetailView):
    # template_name = 'about/update.html'
    model = StartUpBanner
    context_object_name = 'banner'
# Create your views here.
