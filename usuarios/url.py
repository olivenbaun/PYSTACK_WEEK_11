from django.urls import path
from . import views

urlpatters = [
    path('cadstro/', views.cadastro, name="cadastros")
]