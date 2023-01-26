from django.urls import path
from . import views

urlpatterns = [
    path("", views.MemberSignupView.as_view())
]