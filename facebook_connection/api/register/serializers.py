# import self as self
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from register.models import StartUpRegister


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

# def create(self, validated_data):
# 	affiliate_data = validated_data.pop('register')
# 	user = User.objects.create_user(**validated_data)
# 	StartUpRegister.objects.create(user=user, **affiliate_data)
# 	return user


class RegisterCreateSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StartUpRegister
        fields = ('contact_num', 'contact_email', 'user')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**validated_data)

        startUp = StartUpRegister.objects.create(user=user, **validated_data)
        return startUp


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
        fields = ('firstname', 'lastname', 'contact_num', 'contact_email')
