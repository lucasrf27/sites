from django.urls import path
from .views import categoryView
from . import views

urlpatterns = [
    path('', views.HomeView, name='home2'),
    path('categorias', categoryView.as_view(), name='categorias')
    ]
