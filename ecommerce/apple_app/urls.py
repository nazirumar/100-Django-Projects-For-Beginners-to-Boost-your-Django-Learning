from django.urls import path
from apple_app import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'apple'

urlpatterns = [
    path('', views.home, name='index'),
    path('women/', views.womens_view, name='women'),
    path('men/', views.mens_view, name='men'),
    path('shop/', views.shop_view, name='shop'),
    path('product-detail/<slug:slug>/', views.product_detail, name='product-detail'),
    path('add-to-cart/<slug:slug>/', views.add_cart_view, name='add-to-cart'),
    path('order-summary', views.order_summary, name='order-summary'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
    path('remove_single_item_from_cart/<slug>/', views.remove_single_item_from_cart, name='remove_single_item_from_cart'),
    path('checkout',views.CheckoutView.as_view(), name='checkout'),
    path('add-coupon',views.AddCouponView.as_view(), name='add-coupon'),
    path('liked/<str:pk>', views.liked_view, name='liked'),
    path('contact', views.contact, name='contact'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)