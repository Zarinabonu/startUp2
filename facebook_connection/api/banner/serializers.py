from rest_framework.serializers import ModelSerializer
from startUpBanner.models import StartUpBanner

class BannerCreateSerializer(ModelSerializer):
	class Meta:
		model = StartUpBanner
		fields = ('title', 'description', 'data')


class BannerListSerializer(ModelSerializer):
	class Meta:
		model = StartUpBanner
		fields = ('title', 'description', 'data')
