from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.check_eligibility, name='check_eligibility'),
]
