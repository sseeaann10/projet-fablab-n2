from django import forms
from .models import ContactForm
from captcha.fields import ReCaptchaField
class ContactFormForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message','subject','numero']