from django.shortcuts import render, get_object_or_404
from shopping_cart.models import Order
from .models import Profile



def my_profile(request):
    on_profile = Profile.objects.filter(user=request.user).first()
    on_order = Order.objects.filter(is_ordered=True, owner=on_profile)



