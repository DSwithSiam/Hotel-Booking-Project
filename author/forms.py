from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']

    # def save(self):
    #     username = self.cleaned_data['username']
    #     first_name = self.cleaned_data['first_name']
    #     last_name = self.cleaned_data['last_name']
    #     email = self.cleaned_data['email']
    #     password = self.cleaned_data['password']
        
    #     account = User(username = username, email=email, first_name = first_name, last_name = last_name)
    #     account.set_password(password)
    #     account.is_active = False
    #     account.save()
    #     return account
        
class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email',]
        
class DepositForm(forms.Form):
    deposit = forms.DecimalField(max_digits=5, decimal_places=1)