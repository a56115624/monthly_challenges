from django.urls import path
from . import views


urlpatterns = [
    path("<int:month>", views.challenges_month_by_number),
    path("<str:month>", views.challenges_month)
]
