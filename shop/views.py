from django.shortcuts import redirect, render
from .models import Product, ContactForm, ImageSetter, Image,AboutUs,ContactUs,Footer,ContactUsPage
from django.core.paginator import Paginator
from .forms import ContactFormForm
from django.core.mail import send_mail
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        product_object = product_object.filter(name__icontains=item_name)

    paginator_object = Paginator(product_object, 2)
    page= request.GET.get('page')
    product_object = paginator_object.get_page(page)

    return render(request, 'shop/index.html', {'product_object':product_object})
    

def detail(request,myid):
    product_object = Product.objects.filter(id=myid)
    return render(request, 'shop/detail.html', {'product':product_object[0]})

def acceuil(request):
    # background_image = ImageSetter.objects.get(name='Background Image')
    # body_image = ImageSetter.objects.get(name='Body Image')
    # context = {
    #     'background_image': background_image.image.url,
    #     'body_image': body_image.image.url,
    #     # add more context variables as needed
    # }
    pics = Image.objects.all()
    aboutuspics = AboutUs.objects.all()
    contactuspics = ContactUs.objects.all()
    footerpics = Footer.objects.all()
    contactuspagepics = ContactUsPage.objects.all()
    return render(request, 'shop/acceuil.html ', {'pics':pics , 'aboutuspics':aboutuspics , 'contactuspics':contactuspics , 'footerpics':footerpics, 'contactuspagepics':contactuspagepics})

# def contact(request):
#     return render(request, 'shop/contact.html')

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']
            numbero = form.cleaned_data['numero']
            send_mail(
            'Thanks for contacting us',
            f'Thank you for contacting us, {name}! We have received your message about {subject} and will get back to you shortly.',
            'your_email@gmail.com', # Change this to your email address
            [email],
            fail_silently=False,
        )
        
        # Send email to admin
        send_mail(
            'New message from your website',
            f'You have received a new message from {name} ({email}): {message} {numbero}',
            'your_email@gmail.com', # Change this to your email address
            ['seantesst01@gmail.com'], # Change this to the admin's email address
            fail_silently=False,
        )
        return render(request, 'shop/success.html')
    else:
        form = ContactFormForm()
    return render(request, 'shop/contact.html', {'form': form})



    #    if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         message = form.cleaned_data['message']
    #         contact = ContactForm(name=name, email=email, message=message)
    #         contact.save()
    #         return render(request, 'shop/success.html')
    #     else:
    #         form = ContactFormForm()
    #         context = {'form': form}
    #     return render(request, 'contact.html', context)