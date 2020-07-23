from rest_framework import serializers
from .models import *

# class MediaSerializer(serializers.ModelSerializer):
#     #product = ProductSerializer(required=True)
#     product_image = serializers.ImageField(
#     	max_length=None, use_url=True, allow_null=True, required=False)

#     class Meta:
#         model = Media
#         fields = ('product_image',)

# class ProductSerializer(serializers.ModelSerializer):
# 	product=MediaSerializer(required=True)
# 	class Meta:
# 		model = Product
# 		fields = ("id", "product_name",'product')


# class CategorySerializer(serializers.ModelSerializer):
# 	product=ProductSerializer(many=True,read_only=True)

# 	class Meta:
# 		model = Category
# 		fields = ("id", "category_name", 'product')



# class CategorySerializer1(serializers.ModelSerializer):
# 	product=ProductSerializer(many=True,read_only=True)
#     #parent_cat = serializers.PrimaryKeyRelatedField(many=True)

# 	class Meta:
# 		model = Category
# 		fields = ("id", "category_name",'product')


class MediaSerializer(serializers.ModelSerializer):
    #product = ProductSerializer(required=True)
    product_image = serializers.ImageField(
    max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = Media
        fields = ('product_image',)

class ProductSerializer(serializers.ModelSerializer):
	product=MediaSerializer(required=True)
	class Meta:
		model = Product
		fields = ("id", "product_name",'product')


class CategorySerializer(serializers.ModelSerializer):
	product=ProductSerializer(many=True,read_only=True)


	class Meta:
		model = Category
		fields = ("id", "category_name", 'product')
