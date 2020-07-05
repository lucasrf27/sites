from django.urls import path
from . import views


urlpatterns = [
    #FRONT#
    path('home/', views.amp_home, name='home_product'),
    path('list/', views.list_view, name='list_product'),
    path('list/kids/', views.kids_list_view, name='kids_list_product'),
    path('list/adult/', views.adult_list_view, name='adult_list_product'),
    path('detail/<int:id>', views.detail_view, name='detail_product'),
    path('contact/', views.contact_view, name='contact'),
    path('chat/', views.chat_view, name='chat'),
    #test#
    path('test', views.test_view, name='test_view'),
    #BACK#
    path('admin', views.admin_view, name='admin_product'),
    path('add_product', views.add_product, name='add_product'),
    path('add_modelo', views.add_modelo, name='add_modelo'),
    path('update_product/<int:pk>', views.update_product, name='update_product'),
    path('delete_product/<int:pk>', views.delete_product, name='delete_product'),
    path('add_banner/', views.add_banner, name='add_banner')
]
