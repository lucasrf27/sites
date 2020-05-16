from django.urls import path
from .views import HomeView
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('car_add/', views.addProduto2, name='add'),
    path('car_add2/', views.addProduto3, name='add2')
    ]
