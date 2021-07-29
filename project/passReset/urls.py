from django.urls import path
from . import views

urlpatterns = [
    path("password_reset/", views.password_reset_request, name="password_reset"),
]
