from django.urls import path

from common import views

urlpatterns = [
    path('',views.common,name='home'),
    path('like/<int:photo_id>',views.like_view,name='like'),
    path('share/<int:photo_id>',views.share_view,name='share')
]


