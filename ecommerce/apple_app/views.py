from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from apple_app.models import Category, Order, OrderItem, Product,Liked, Address, Payment, Coupon, Refund, UserProfile
from apple_app.forms import ContactForm, CheckoutForm, CouponForm, PaymentForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
# Create your views here.
from django.core.exceptions import ObjectDoesNotExist

from django.views import View


@login_required
def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(Q(category__title__icontains="Men`s") | Q(category__title__icontains="Women`s")).only('title', 'price', 'image', 'label')
    hot_trend = Product.objects.filter(Q(category__title__icontains="Accessories") | Q(category__title__icontains="Cosmetics")).only('title', 'price', 'image', 'label')
    best_seller = Product.objects.filter(Q(category__title__icontains="Accessories") | Q(category__title__icontains="Cosmetics")).only('title', 'price', 'image', 'label')
    feature = Product.objects.filter(Q(category__title__icontains="Accessories") | Q(category__title__icontains="Cosmetics")).only('title', 'price', 'image', 'label')
    context = {
        'categories':categories,
        'products':products,
        'hot_trend' :hot_trend,
        'best_seller': best_seller,
        'feature':feature
        }
    return render(request, 'index.html', context)

@login_required
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context ={
        'product':product,
    }
    return render(request, 'product-details.html',context)

@login_required
def shop_view(request):
    shop = Product.objects.all()
    context = {
        'shop':shop
    }
    return render(request, 'shop.html', context)

@login_required
def liked_view(request, pk):
    product =get_object_or_404(Product, pk=pk)
    liked_post, created= Liked.objects.get_or_create(
        product=product,
        user = request.user,
        like = True
        )
    liked_post.save()
    if not created:  #If get_or_create() function not created a new LikedPost
        liked_post.delete()
        messages.info(request, "This post was disliked.")
    else: # If created a new LikedPost => this user did not like this post 
        liked_post.save()
        messages.info(request, "This post was liked.")
    return redirect('apple:index')

@login_required
def womens_view(request):
    categories = Category.objects.filter(title__contains="Women`s")
    products = Product.objects.only('title', 'price', 'image', 'label').filter(category__title__contains="Women`s")
    context = {
        'categories':categories,
        'products':products,
        }
    return render(request, 'women_page.html', context)

@login_required
def mens_view(request):
    categories = Category.objects.filter(title__contains="Men`s")
    products = Product.objects.only('title', 'price', 'image', 'label').filter(category__title__contains="Men`s")
    context = {
        'categories':categories,
        'products':products,
        }
    return render(request, 'men_page.html', context)

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Successfuly Send we will Contact you Letter !')
            return redirect('apple:contact')
    return render(request, 'contact.html')

@login_required
def add_cart_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item = product,
        user = request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=product.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("apple:order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("apple:index")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("apple:index")

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("apple:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("apple:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("apple:product", slug=slug)

@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("apple:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("apple:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("apple:product", slug=slug)
    
@login_required
def order_summary(request):
    try:
        order = Order.objects.get(user=request.user, ordered=False)
        print(order.coupon)
        context = {
            'object': order,
            'couponForm':CouponForm(),
            'DISPLAY_COUPON_FORM': True
        }
        return render(request,'shop-cart.html', context)
    except ObjectDoesNotExist:
        messages.warning(request, "You do not have an active order")
        return redirect("apple:index")

@login_required
def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid



class CheckoutView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            form = CheckoutForm()
            context = {
                'form': form,
                'couponform': CouponForm(),
                'order': order,
                'DISPLAY_COUPON_FORM': True
            }

            shipping_address_qs = Address.objects.filter(
                user=self.request.user,
                address_type='S',
                default=True
            )
            if shipping_address_qs.exists():
                context.update(
                    {'default_shipping_address': shipping_address_qs[0]})

            billing_address_qs = Address.objects.filter(
                user=self.request.user,
                address_type ='B',
                default=True
            )
            if billing_address_qs.exists():
                context.update(
                    {'default_billing_address': billing_address_qs[0]})
            return render(self.request, "checkout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("apple:checkout")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():

                use_default_shipping = form.cleaned_data.get(
                    'use_default_shipping')
                if use_default_shipping:
                    print("Using the defualt shipping address")
                    address_qs = Address.objects.filter(
                        user=self.request.user,
                        address_type='S',
                        default=True
                    )
                    if address_qs.exists():
                        shipping_address = address_qs[0]
                        order.shipping_address = shipping_address
                        order.save()
                    else:
                        messages.info(
                            self.request, "No default shipping address available")
                        return redirect('apple:checkout')
                else:
                    print("User is entering a new shipping address")
                    shipping_address1 = form.cleaned_data.get(
                        'shipping_address')
                    shipping_address2 = form.cleaned_data.get(
                        'shipping_address2')
                    shipping_country = form.cleaned_data.get(
                        'shipping_country')
                    shipping_zip = form.cleaned_data.get('shipping_zip')

                    if is_valid_form([shipping_address1, shipping_country, shipping_zip]):
                        shipping_address = Address(
                            user=self.request.user,
                            street_address=shipping_address1,
                            apartment_address=shipping_address2,
                            country=shipping_country,
                            zip=shipping_zip,
                            address_type='S'
                        )
                        shipping_address.save()

                        order.shipping_address = shipping_address
                        order.save()

                        set_default_shipping = form.cleaned_data.get(
                            'set_default_shipping')
                        if set_default_shipping:
                            shipping_address.default = True
                            shipping_address.save()

                    else:
                        messages.info(
                            self.request, "Please fill in the required shipping address fields")

                use_default_billing = form.cleaned_data.get(
                    'use_default_billing')
                same_billing_address = form.cleaned_data.get(
                    'same_billing_address')

                if same_billing_address:
                    billing_address = shipping_address
                    billing_address.pk = None
                    billing_address.save()
                    billing_address.address_type = 'B'
                    billing_address.save()
                    order.billing_address = billing_address
                    order.save()

                elif use_default_billing:
                    print("Using the defualt billing address")
                    address_qs = Address.objects.filter(
                        user=self.request.user,
                        address_type='B',
                        default=True
                    )
                    if address_qs.exists():
                        billing_address = address_qs[0]
                        order.billing_address = billing_address
                        order.save()
                    else:
                        messages.info(
                            self.request, "No default billing address available")
                        return redirect('apple:checkout')
                else:
                    print("User is entering a new billing address")
                    billing_address1 = form.cleaned_data.get(
                        'billing_address')
                    billing_address2 = form.cleaned_data.get(
                        'billing_address2')
                    billing_country = form.cleaned_data.get(
                        'billing_country')
                    billing_zip = form.cleaned_data.get('billing_zip')

                    if is_valid_form([billing_address1, billing_country, billing_zip]):
                        billing_address = Address(
                            user=self.request.user,
                            street_address=billing_address1,
                            apartment_address=billing_address2,
                            country=billing_country,
                            zip=billing_zip,
                            address_type='B'
                        )
                        billing_address.save()

                        order.billing_address = billing_address
                        order.save()

                        set_default_billing = form.cleaned_data.get(
                            'set_default_billing')
                        if set_default_billing:
                            billing_address.default = True
                            billing_address.save()

                    else:
                        messages.info(
                            self.request, "Please fill in the required billing address fields")

                payment_option = form.cleaned_data.get('payment_option')

                if payment_option == 'S':
                    return redirect('apple:payment', payment_option='stripe')
                elif payment_option == 'P':
                    return redirect('apple:payment', payment_option='paypal')
                else:
                    messages.warning(
                        self.request, "Invalid payment option selected")
                    return redirect('apple:checkout')
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("apple:order-summary")

@login_required     
def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except Coupon.DoesNotExist:
        messages.info(request, "This coupon does not exist")
        return redirect("apple:order-summary")


class AddCouponView(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(
                    user=self.request.user, ordered=False)
                order.coupon = get_coupon(self.request, code)
                order.save()
                messages.success(self.request, "Successfully added coupon")
                return redirect("apple:order-summary")
            except ObjectDoesNotExist:
                messages.info(self.request, "You do not have an active order")
                return redirect("apple:order-summary")
        return redirect("apple:order-summary")
    