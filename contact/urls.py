from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add-contact/', views.addcontact, name="add-contact"),
    path('profile/<str:pk>', views.contactprofile, name="contactprofile"),
    path('editcontact/<str:pk>', views.editcontact, name="editcontact"),
    path('deletecontact/<str:pk>', views.deletecontact, name="deletecontact"),
]