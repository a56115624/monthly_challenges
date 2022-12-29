from django.urls import path
from . import views


urlpatterns = [
    path("<month>", views.challenges_month)
]
