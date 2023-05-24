from django.urls import path
from . import views

urlpatterns = [
    path('recom/', views.calculator, name='calculator'),
]
