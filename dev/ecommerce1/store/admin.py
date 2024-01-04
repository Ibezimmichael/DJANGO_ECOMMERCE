from django.contrib import admin
from .models import Category, Product
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

 
class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = 'description'
    

@admin.register(Product)
class ProductAdmin(SummerAdmin, admin.ModelAdmin):
    list_display = ["title", "brand", "price", "category"]
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
