from django.urls import path, include

from photos import views

urlpatterns = [
    path('add/',views.PhotoAddView.as_view(),name='add-photo'),
    path('<int:pk>/',include([
        path('',views.PhotoDetailsView.as_view(),name='photo-details'),
        path('edit/',views.PhotoEditView.as_view(),name='photo-edit'),
        path('delete/',views.PhotoDeleteView.as_view(),name='photo-delete')
    ]))
]