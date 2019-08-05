from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from startUpBanner.models import StartUpBanner
from .serializers import BannerCreateSerializer,BannerListSerializer

class Banner_Create(CreateAPIView):
    queryset = StartUpBanner.objects.all()
    serializer_class = BannerCreateSerializer

class Banner_Update(UpdateAPIView):
    queryset = StartUpBanner.objects.all()
    serializer_class = BannerCreateSerializer
    

class Banner_Delete(DestroyAPIView):
    queryset = StartUpBanner.objects.all()
    lookup_url_kwargs ='id'  

class Banner_List(ListAPIView): 
	serializer_class = BannerListSerializer
	model = StartUpBanner

	def get_queryset(self):
		u = StartUpBanner.objects.filter().order_by('-data')[:3]   
		return u

class BannerAll_list(ListAPIView):
    serializer_class = BannerListSerializer
    model = StartUpBanner        