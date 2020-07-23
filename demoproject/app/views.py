from django.shortcuts import render,redirect
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework import generics
from .models import *
from django_filters.rest_framework import DjangoFilterBackend

# class UserDetail(APIView):

# 	def get_object(self, pk):
# 		try:
# 			return Category.objects.filter(shop_id=pk)
# 		except Category.DoesNotExist:
# 			raise Http404
# 	def get(self, request, pk, format=None):
# 		category = self.get_object(pk)
# 		serializer_class = CategorySerializer(category,many=True)
# 		return Response({"status":status.HTTP_200_OK,"data":serializer_class.data,"message": True})


	# def get(self,request,pk):

	# 	try:
	# 		c_id=Category.objects.filter(shop_id=pk)
	# 		serializer_class = CategorySerializer(c_id,many=True)

	# 		return Response({"status":200,"data":serializer_class.data,"message": True})
	# 	except Category.DoesNotExit as e:
	# 		return  None

		# c_id=Category.objects.filter(shop_id=pk)
		#print(c_id)

		#queryset = Product.objects.filter(category_id=pk)
		#print(queryset)
		#media=Media.objects.filter(product_id=pk)
		#print(media)
		#serializer_class = ProductSerializer(queryset,many=True)
		# serializer_class = CategorySerializer(c_id,many=True)

		# print(serializer_class.data)
		# return Response(serializer_class.data)



class ProductList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    print('serializers',serializer_class)
    #queryset=Category.objects.all()
    def get_queryset(self):
     	queryset=Category.objects.all()
     	shop_id=self.request.query_params.get('shop_id')
     	data=queryset.filter(shop_id=shop_id)
     	return data

    def list(self, request):
    	queryset = self.get_queryset()
    	serializer = CategorySerializer(queryset, many=True)

    	return Response({"status":status.HTTP_200_OK,"data":serializer.data[0],"message": True})


    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['shop_id']