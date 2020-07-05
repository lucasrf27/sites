from django.urls import path
from . import views


urlpatterns = [
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('order_summary/', views.order_details, name='order_summary'),
    path('success/', views.success, name='purchase_success'),
    path('item/delete/<int:id>', views.delete_from_cart, name='delete_item'),
    path('checkout/', views.checkout, name='checkout'),
]