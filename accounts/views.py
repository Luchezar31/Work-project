from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView

from accounts.forms import AppUserCreationForm, AppLoginForm, ProfileEditForm
from accounts.models import AppUserModel, Profile
from common.mixins import ProfileOwnerOnlyAccessMixin




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


class AppLogoutView(LogoutView):
    pass

class ProfileEditView(LoginRequiredMixin,ProfileOwnerOnlyAccessMixin,UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'



    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk':self.object.pk
            }
        )


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'accounts/profile-details-page.html'


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context['total_likes'] = self.object.user.photo_set.annotate(
            num_likes=Count('like')
        ).aggregate(
            total_likes=Sum('num_likes')
        ).get(
            'total_likes'
        ) or 0

        context['total_photos'] = self.object.user.photo_set.count()

        context['total_pets'] = self.object.user.pet_set.count()

        return context


class DeleteProfileView(DeleteView):
    model = Profile
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset = ...):
        object = self.request.user

        return object
