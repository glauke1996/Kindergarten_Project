from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from . import models


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "w-100 takasa-login rounded"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "w-100 takasa-login rounded"})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = "이메일"
        self.fields["password"].label = "패스워드"

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("잘못된 패스워드 입니다"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("유저가 존재하지 않습니다"))


class SignUpForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "w-100 takasa-login rounded"}),
        max_length=80,
        label="닉네임",
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "w-100 takasa-login rounded"}),
        max_length=80,
        label="이름",
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "w-100 takasa-login rounded"}),
        max_length=80,
        label="성",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "w-100 takasa-login rounded"}),
        label="이메일",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "w-100 takasa-login rounded"}),
        label="패스워드",
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "w-100 takasa-login rounded"}),
        label="패스워드 확인",
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = models.User.objects.get(username=username)
            raise forms.ValidationError("이 닉네임은 이미 등록되어 있습니다")
        except models.User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            user = models.User.objects.get(email=email)
            raise forms.ValidationError("이 이메일은 이미 등록되어 있습니다")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다")
        return password

    def save(self):

        username = self.cleaned_data.get("username")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user = models.User.objects.create_user(username, email, password)

        user.first_name = first_name
        user.last_name = last_name
        user.save()
