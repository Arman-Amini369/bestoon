from django import forms

class UserRegisterForm(forms.Form):
    first_name = forms.CharField(label="نام")
    last_name = forms.CharField(label="نام خانوادگی")
    username = forms.CharField(label="نام کاربری")
    email = forms.EmailField(label="ایمیل")
    password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور")

class UserLoginForm(forms.Form):
    username = forms.CharField(label="نام کاربری")
    password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور")