from django.shortcuts import render,redirect,get_object_or_404
from products.models import Product
from .models import CartItem
from django.views.decorators.http import require_POST


def cart(request):
    cart_items = CartItem.objects.filter(user=request.user).order_by('id')

    total = 0
    for item in cart_items:
        total += item.subtotal()

    return render(request,'cart.html',{
        'cart_items': cart_items,
        'total': total,
    })

@require_POST
def add_to_cart(request,product_id):
    product = get_object_or_404(Product,id=product_id)

    cart_item,created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/')

@require_POST
def remove_from_cart(request,item_id):
    item = get_object_or_404(CartItem,id=item_id,user=request.user)
    item.delete()
    return redirect('cart')

@require_POST
def decrease_quantity(request,item_id):
    item = get_object_or_404(CartItem,id=item_id,user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart')

@require_POST
def increase_quantity(request,item_id):
    item = get_object_or_404(CartItem,id=item_id,user=request.user)
    item.quantity += 1
    item.save()
    return redirect('cart')

@require_POST
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_items.delete()
    return render(request,'success.html')