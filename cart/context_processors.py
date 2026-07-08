from .models import CartItem

def cart_count(request):
    cart_items = CartItem.objects.filter(user=request.user)

    cart_count = 0

    for item in cart_items:
        cart_count += item.quantity

    return {
        'cart_count': cart_count
    }