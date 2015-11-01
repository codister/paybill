from django import forms
from django.contrib.auth.models import User
from pb.models import Request, Payment, Merchent




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class MerchentForm(forms.ModelForm):
    class Meta:
        model = Merchent
        fields = ('contact_num', 'cnic_photo', 'cinc_selfi_photo', 'billing_id_number')


