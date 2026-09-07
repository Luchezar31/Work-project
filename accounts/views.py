from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import AppUserCreationForm, AppLoginForm
from accounts.models import AppUserModel


def register_account(request):
    return render(request,'accounts/register-page.html')


class RegisterView(CreateView):
    model = AppUserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        self.object = form.save()

        login(self.request,self.object)
        return HttpResponseRedirect(self.get_success_url())


class AppLoginView(LoginView):
    form_class = AppLoginForm
    template_name = 'accounts/login-page.html'




def login_account(request):
    return render(request,'accounts/login-page.html')

def profile_details(request,pk):
    return render(request,'accounts/profile-details-page.html')

def profile_edit(request,pk):
    return render(request,'accounts/profile-edit-page.html')

def profile_delete(request,pk):
    return render(request,'accounts/profile-delete-page.html')


