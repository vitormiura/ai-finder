from django.urls import path

from contacts import views

urlpatterns = [
    path('/contacts', views.ContactView.as_view(), name='contact')
]
