from django.contrib.auth.views import LoginView
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('register/',views.RegisterView.as_view(),name='register-account'),
    path('login/',views.AppLoginView.as_view(),name='login'),
    path('profile/<int:pk>/',include([
        path('',views.profile_details,name='profile-details'),
        path('edit/',views.profile_edit,name='profile-edit'),
        path('delite/',views.profile_delete,name='profile-delite')
    ]))


]