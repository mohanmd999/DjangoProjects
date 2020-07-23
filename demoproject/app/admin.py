from django.contrib import admin

# Register your models here.
from .models import shop,Category,Product,Media


admin.site.register(shop)
admin.site.register(Category)

admin.site.register(Product)

admin.site.register(Media)

