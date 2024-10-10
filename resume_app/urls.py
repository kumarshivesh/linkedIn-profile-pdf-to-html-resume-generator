# resume_app/urls.py
from django.urls import path
from . import views

app_name = 'resume_app'

urlpatterns = [
  path('', views.upload_pdf, name='upload_pdf'),
]