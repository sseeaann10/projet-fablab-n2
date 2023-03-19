from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    
    category = models.ForeignKey(
        Category, related_name="categorie", on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    info = models.TextField(default='')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name
    
# class Contact(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     message = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-date_added']

#     def __str__(self):
#         return self.name

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=200,null=True, blank=True)
    numero = models.IntegerField(max_length=15,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ImageSetter(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')
    # Add more fields as needed

    def __str__(self):
        return self.name
    

class Image(models.Model): # This is the model for the banner image
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/%y', default='media/b9ddc38e5835fac634678392530003dc.png')
    # Add more fields as needed

    def __str__(self):
        return self.caption
    

class AboutUs(models.Model): # This is the model for the banner image
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/%y', default='media/b9ddc38e5835fac634678392530003dc.png')
    # Add more fields as needed

    def __str__(self):
        return self.caption
class ContactUs(models.Model): # This is the model for the banner image
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/%y', default='media/b9ddc38e5835fac634678392530003dc.png')
    # Add more fields as needed

    def __str__(self):
        return self.caption   
    
class Footer(models.Model): # This is the model for the banner image
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/%y', default='media/b9ddc38e5835fac634678392530003dc.png')
    # Add more fields as needed

    def __str__(self):
        return self.caption

class Carousel(models.Model): 
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/%y', default='media/b9ddc38e5835fac634678392530003dc.png')

    def __str__(self):
        return self.caption