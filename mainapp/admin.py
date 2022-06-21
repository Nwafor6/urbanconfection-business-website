from django.contrib import admin
from .models import Product, ProductVideo

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['title','price', 'category']
    prepopulated_fields={'slug': ('title',)}


class ProductVideoAdmin(admin.ModelAdmin):
    list_display=['video_title', 'date']
    prepopulated_fields={'slug': ('video_title',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVideo, ProductVideoAdmin)
