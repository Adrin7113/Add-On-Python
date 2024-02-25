from django import forms

from addOn.models import ContactUsModel,LoginModel,RegModel

class ContactUsForm(forms.ModelForm):
    class Meta:
        model=ContactUsModel
        fields=['name','email','contact','message','place']

class LoginForm(forms.ModelForm):
    class Meta:
        model=LoginModel
        fields=['username','password']

class RegForm(forms.ModelForm):
    class Meta:
        model=RegModel
        fields=['FName','LName','PhoneNo','email']

