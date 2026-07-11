from .models import CartItem

def cart_count(request):
    if not request.user.is_authenticated:
        return{
            'cart_count': 0
        }

    cart_items = CartItem.objects.filter(user=request.user)

    total_quantity = 0
    for item in cart_items:
        total_quantity += item.quantity

    return {
        'cart_count': total_quantity
    }