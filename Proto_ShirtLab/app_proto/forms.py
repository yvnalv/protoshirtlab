from django import forms
from app_proto.models import SLUser, AdminUser
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    class Meta():
        model = SLUser
        fields = '__all__'

class UserBaseForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):

    portofolio = forms.URLField(required=False)
    user_pics = forms.ImageField(required=False)

    class Meta():
        model = AdminUser
        fields = ('portofolio','user_pics')
