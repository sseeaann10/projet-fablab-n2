from django.contrib import admin
from .models import Category, Product, ContactForm, ImageSetter, Image,Carousel,AboutUs,ContactUs,Footer,ContactUsPage

# Register your models here.

class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'date_added']

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'date_added']

class AdminContactForm(admin.ModelAdmin):
    list_display = ['name', 'email','created_at']

class AdminImageSetter(admin.ModelAdmin):
    list_display = ['name', 'image']



admin.site.register(ContactForm, AdminContactForm)
# admin.site.register(Category, AdminCategory)
# admin.site.register(Product, AdminProduct)
# admin.site.register(ImageSetter, AdminImageSetter)
admin.site.register(Image)
# admin.site.register(Carousel)
admin.site.register(AboutUs)
admin.site.register(ContactUs)
admin.site.register(Footer)
admin.site.register(ContactUsPage)