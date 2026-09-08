from django.contrib.auth.views import LoginView
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('register/',views.RegisterView.as_view(),name='register-account'),
    path('login/',views.AppLoginView.as_view(),name='login'),
    path('logout/',views.AppLogoutView.as_view(),name='logout'),
    path('profile/<int:pk>/',include([
        path('',views.ProfileDetailsView.as_view(),name='profile-details'),
        path('edit/',views.ProfileEditView.as_view(),name='profile-edit'),
        path('delite/',views.profile_delete,name='profile-delite')
    ]))


]