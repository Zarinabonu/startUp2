from rest_framework.serializers import ModelSerializer
from register.models import StartUpRegister

class RegisterCreateSerializer(ModelSerializer):
	class Meta:
		model = StartUpRegister
		fields = ('username', 'password', 'contact_num','contact_email')

# 	def create(self,validated_data):
#         doc = StartUpRegister(**validated_data)
#         doc.save()
#         firstname = self.context['request'].data.get('firstname')
#         lastname = self.context['request'].data.get('lastname')
#         # title  = self.context['request'].data.get('title')
#         # description = self.context['request'].data.get('description')
#         # photo= self.context['request'].FILES.get('photo')
#         # photo = ?photo.url
#         print('AAA',photo)
#         # photo = photo.absolute
#         # doc.photo = photo
#         # doc.firstname = firstname
#         # return request.build_absolute_uri(photo)
#         # print('doc.photo',doc.photo)

#         msg = EmailMessage(title,
#                 description,
#                 settings.EMAIL_HOST_USER,
#                 ['zarinabonu199924@gmail.com'])
# # , content=None, mimetype=None

#         msg.attach_file(BASE_DIR,photo)
#         msg.send()	


class RegisterListSerializer(ModelSerializer):
	class Meta:
		model = StartUpRegister
		fields = ('firstname', 'lastname', 'contact_num','contact_email')