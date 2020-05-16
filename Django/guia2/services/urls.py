from django.urls import path, include
from . import views
from .views import ParceirosView, ParceiroUpdate

urlpatterns = [
    path('home/', views.home_view, name='home2'),
    path('parceiro/', views.parceirosview, name='parceiro2'),
    path('parceiro/detail/<int:pk>', views.parceirosview, name='parceiro_detail2'),
    path('parceiro/add', views.parceiros_create, name='add_parceiro2'),
    path('parceiro/servicos/add', views.service_create, name='service_add2'),
    
    
    
    #test generic
    path('parceiro/detail2/<int:pk>', ParceirosView.as_view(), name='parceiro_detail22'),
    path('parceiro/update/<int:pk>', ParceiroUpdate.as_view(), name='update_parceiro2'),
]
