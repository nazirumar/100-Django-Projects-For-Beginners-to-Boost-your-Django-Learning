from apple_app.models import Liked, OrderItem
from django import template
register = template.Library()
from django.core.exceptions import ObjectDoesNotExist


@register.filter
def customtags(request):
    liked_count = None
    orders_count = None
    try:
        if request.user.is_authenticated:
            liked_count = Liked.objects.all().filter(user=request.user).count()
            orders_count = OrderItem.objects.all().filter(user=request.user).count()
    except ObjectDoesNotExist:
        liked_count = None
    context = {'liked_count': liked_count,
               'orders_count':orders_count
               }
    return context
   