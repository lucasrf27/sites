from django.shortcuts import render
from .models import Item, Pedido
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from products.models import Produto
from django.contrib import messages
from django.urls import reverse
from .extras import generate_order_id
from accounts.forms import ProfileForm
from django.shortcuts import HttpResponse
from accounts.models import Profile


User = get_user_model()


@login_required(login_url='/accounts/automatic')
def add_to_cart(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(User, username=request.user)
    # filter products by id
    product = Produto.objects.filter(id=kwargs.get('id', "")).first()
    # create orderItem of the selected product
    # create order associated with the user
    user_order, status = Pedido.objects.get_or_create(owner=user_profile, is_ordered=False)
    pedido = Pedido.objects.get(owner=user_profile, is_ordered=False)
    if Item.objects.filter(product=product, order=user_order).exists():
        item = Item.objects.get(product=product, order=user_order)
        item.quantity += 1
        item.save()
    else:
        Item.objects.create(product=product, order=user_order)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect(reverse('list_product'))



@login_required
def delete_from_cart(request, id):
    item_to_delete = Item.objects.get(pk=id)
    if item_to_delete.quantity != 1:
        item_to_delete.quantity -= 1
        item_to_delete.save()
    else:
        item_to_delete.delete()
    return redirect(reverse('order_summary'))


def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(User, username=request.user)
    pedido = Pedido.objects.filter(owner=user_profile, is_ordered=False)
    if pedido.exists():
        return pedido[0]



@login_required
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    order_items = existing_order.order_items.filter(is_ordered=False)

    context = {
        'existing_order': existing_order,
        'order_items': order_items,
    }
    if request.user_agent.is_mobile:
        return render(request, 'amp/cart_items.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'desktop/cart_items.amp.html', context)
    else:
        return render (request, 'amp/cart_items.amp.html', context)


@login_required
def checkout(request):
    existing_order = get_user_pending_order(request)
    order_items = existing_order.order_items.filter(is_ordered=False)
    prof, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=prof)
        if form.is_valid():
            form.save()
            return redirect('../success')
            
    else:
        form = ProfileForm()
    context = {
        'order_items': order_items,
        'existing_order': existing_order,
        'form': form,
        'prof': prof
    }
    if request.user_agent.is_mobile:
        return render(request, 'amp/checkout.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'desktop/checkout.amp.html', context)
    else:
        return render (request, 'amp/checkout.amp.html', context)


def success(request):
    existing_order = get_user_pending_order(request)
    existing_order.is_ordered = True
    existing_order.save()
    order_items = existing_order.order_items.filter(is_ordered=False)
    for item in order_items:
        item.is_ordered=True
        item.save()
    
    if request.user_agent.is_mobile:
        return render(request, 'amp/success.amp.html')
    elif request.user_agent.is_pc:
        return render (request, 'desktop/success.amp.html')
    else:
        return render (request, 'amp/success.amp.html')