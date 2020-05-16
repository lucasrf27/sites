from django.urls import path
from . import views
from .views import DeleteProduct, UpdateProduct, AdminView


urlpatterns = [
    #FRONT#
    path('home/', views.amp_home, name='home_product'),
    path('list/', views.list_view, name='list_product'),
    path('kids_list/', views.kids_list_view, name='kids_list_product'),
    path('adult_list/', views.adult_list_view, name='adult_list_product'),
    path('detail/<int:pk>', views.detail_view, name='detail-product'),

    #test#
    path('test', views.test_view, name='test_view'),
    #BACK#
    path('admin', AdminView.as_view(), name='admin_product'),
    path('add_product', views.add_product, name='add_product'),
    path('add_modelo', views.add_modelo, name='add_modelo'),
    path('update_product/<int:pk>', UpdateProduct.as_view(), name='update_product'),
    path('delete_product/<int:pk>', DeleteProduct.as_view(), name='delete_product'),
    path('add_banner/', views.add_banner, name='add_banner')
]
