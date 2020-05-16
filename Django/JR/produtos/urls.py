from django.urls import path
from .views import HomeView, addProduto
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', views.addProduto, name='add')
    ]
