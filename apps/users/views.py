import braintree
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoginForm, NewUserForm, Profileupdate
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView

from django.views.generic.base import TemplateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib.auth import get_user_model


from . import forms

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print(form.data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect(reverse("apps:listing:list"))
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(
        request=request,
        template_name="auth/register.html",
        context={"register_form": form},
    )


def login_request(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(reverse("apps:listing:list"))
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = LoginForm()
    return render(
        request=request, template_name="auth/login.html", context={"login_form": form}
    )


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect(reverse("apps:listing:list"))

def profile_request(request):
    user = request.user
    return render(request = request, template_name = "userprofile.html", context={"user": user})


class UserDetailView(DetailView):
    template_name = "userprofile.html"
    model = get_user_model()
    slug_field = "username"
    slug_url_kwarg = "username"

@login_required
def profile(request):
    if request.method == 'POST':
        p_form = Profileupdate(request.POST,request.FILES,instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request,'Your Profile has been updated!')
            return redirect('userprofile.html')
    else:
        p_form = Profileupdate(instance=request.user)

    context={'p_form': p_form}
    return render(request, 'userprofile.html',context )

class CurrentUserDetailView(DetailView):
    template_name = "userprofile.html"
    model = get_user_model()
    def get_object(self):
        return self.request.user