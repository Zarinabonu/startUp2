from rest_framework.serializers import ModelSerializer
# from startUpBanner.models import StartUpRegister
# from startUpBanner import models
from startUpBanner.models import StartUpBanner


class BannerCreateSerializer(ModelSerializer):
	class Meta:
		model = StartUpBanner
		fields = ('title', 'description', 'data')

	def create(self, validated_data):
		query = StartUpBanner.objects.create(**validated_data)
		query.user=self.context['request'].user
		query.save()
		print('QUERY',query)
		return query


class BannerListSerializer(ModelSerializer):
	class Meta:
		model = StartUpBanner
		fields = ('title', 'description', 'data')
