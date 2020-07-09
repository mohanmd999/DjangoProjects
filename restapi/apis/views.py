from django.shortcuts import render,redirect
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from .models import Post
from rest_framework import generics
from .parser_fun import *
from django.contrib.auth.models import User
from .serializers import *
from django.contrib.auth import authenticate,login,logout
from rest_framework import viewsets

# # Create your views here.
# class CreateView(APIView):
# 	def post(self,request):
# 		postdata=PostSerializer
# 		if request.POST:
# 			data=post_parser(request)
# 			print(data)
# 		else:
# 			data=request.data
# 		post_data=PostSerializer(data=data)
# 		if post_data.is_valid():
# 			post_data.save()
# 			return Response(post_data.data)
# 		return Response(post_data.errors)



# class GetView(APIView):
# 	def get(self,request):
# 		get_data=Post.objects.all()
# 		print(get_data)
# 		serializers=PostSerializer(get_data,many=True)
# 		return Response(serializers.data)



class UserList(APIView):
	def get(self,request):
		queryset = User.objects.all()
		serializer_class = GetUserSerializer(queryset,many=True)
		return Response(serializer_class.data)


class UserDetail(APIView):
	def get(self,request,pk):
		queryset = Profile.objects.filter(user_id=pk)
		print(queryset)
		serializer_class = GetProfileSerializer(queryset,many=True)
		print(serializer_class.data)
		return Response(serializer_class.data)



class CreateUser(APIView):
	def post(self,request):
		postdata=CreateUserSerializer
		if request.POST:
			data=create_user_parser(request)
		else:
			data=request.data
		#print(data)
		context={'request': request}
		post_data=CreateUserSerializer(data=data,context=context)
		print("post_data",post_data)
		if post_data.is_valid():
			post_data.save()
			return Response(post_data.data)
		return Response(post_data.errors)

def login_view(request):
		request.session["user"] = None
		if request.method=="POST":
			user=authenticate(username=request.POST.get('username'),
			              password=request.POST.get('password'))
			msg=" login successfully"
			if user:
				print(user)
				user_profiles=Profile.objects.filter(user_id=user)
				print(user_profiles)
				if user_profiles:
					user_profile=user_profiles[0]
					request.session['user']={"username":user.username,"id":user_profile.id}
					request.session.set_expiry(150)
					login(request, user)
				return redirect("/dashbord/")
			else:
				return render(request,'login.html',{"msg":"login failed"})
		return render(request,'login.html')


# def dashbord(request):
	
# 	return render(request,'dashbord.html')


class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


def dashbord(request):
	return render(request,'dashbord.html')