from django.db import models

# Create your models here.
class shop(models.Model):
	shop_name=models.CharField(max_length=225)
	shop_location=models.CharField(max_length=225)

	def __str__(self):
		return self.shop_name

class Category(models.Model):
	category_name=models.CharField(max_length=225)
	#parent_cat=models.CharField(max_length=225)
	parent_cat = models.ForeignKey("self", on_delete=models.CASCADE, null=True,
	 blank=True,related_name='subcategories')

	shop_id=models.ForeignKey(shop, on_delete=models.CASCADE)
	def __str__(self):
		return self.category_name

class Product(models.Model):

	product_name=models.CharField(max_length=225)
	category_id=models.ManyToManyField(Category,related_name='product',)

	def __str__(self):
		return self.product_name

class Media(models.Model):

	product_id=models.OneToOneField(Product,on_delete=models.CASCADE,related_name='product',)
	product_image=models.ImageField()

	

# 
