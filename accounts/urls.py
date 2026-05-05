from django.urls import path, include

from accounts import views

urlpatterns = [
    path('register/',views.register_account,name='register-account'),
    path('login/',views.login_account,name='login'),
    path('profile/<int:pk>/',include([
        path('',views.profile_details,name='profile-details'),
        path('edit/',views.profile_edit,name='profile-edit'),
        path('delite/',views.profile_delete,name='profile-delite')
    ]))


]