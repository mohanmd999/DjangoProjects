from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

# class PostSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model=Post
# 		fields ='__all__'

# from django.contrib.auth.models import User

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email']

# class UserSerializer1(serializers.HyperlinkedModelSerializer):

#     phonenumber = serializers.CharField(source='user_information.phonenumber')
#     address = serializers.CharField(source='user_information.address')
#     def create(self, validated_data):
        
#         return user

#     class Meta:
#         model = User

#         fields = ('username', 'password', 'email', 'first_name', 'last_name',
#             'phonenumber', 'address')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('city', 'country')
        extra_kwargs = {'password': {'write_only': True}}


class CreateUserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer()
    print("CreateUserSerializer")
    def create(self, validated_data, instance=None):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.update_or_create(user=user,**profile_data)
        return user
    # def create(self, validated_data):
    # 	profile_data = validated_data.pop('profile')
    # 	user = User.objects.create(**validated_data)
    # 	Profile.objects.create(user=user, **profile_data)
    # 	return user

    class Meta:
        model = User
        fields = ( 'username', 'password', 'email',  'profile')
        # extra_kwargs = {'password': {'write_only': True}}
        # context={'request': request}






class GetProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""
    user = GetUserSerializer()


    class Meta:
        model = Profile
        fields = ( 'city',  'country',  'user')

