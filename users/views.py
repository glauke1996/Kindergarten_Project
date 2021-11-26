from django.http.response import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic import FormView, UpdateView
from django.contrib.auth import authenticate, login, logout
from . import forms
from . import models, mixins

# Create your views here.


class LoginView(mixins.LoggedOutOnlyView, View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            email = form.cleaned_data.get("email")
            for_username = models.User.objects.get(email=email)
            username = for_username.username
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_arg = self.request.GET.get("next")
                print(next_arg)
                if next_arg != None:
                    return redirect(next_arg)
                else:
                    return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(mixins.LoggedOutOnlyView, FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        for_username = models.User.objects.get(email=email)
        username = for_username.username
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(reverse("core:home"))
        return super().form_valid(form)


def ProfileView(request, pk):
    try:
        user = models.User.objects.get(pk=pk)
        if request.method == "GET":
            return render(request, "users/profile.html", {"user": user})
    except models.User.DoesNotExist:
        raise Http404


class UpdateProfileView(mixins.LoggedInOnlyView, UpdateView):
    model = models.User
    template_name = "users/profile-update.html"
    fields = (
        "first_name",
        "last_name",
        "avatar",
        "gender",
        "bio",
        "birth",
    )

    def get_object(self, queryset=None):
        return self.request.user
