from django.urls import path
from cart.views import add_to_cart, cart, checkout, hx_menu_cart, update_cart, hx_cart_total, success


urlpatterns = [
    path('', cart, name='cart'),
    path('success/', success, name='success'),
    path('checkout/', checkout, name='checkout'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update-cart/<int:product_id>/<str:action>/', update_cart, name='update_cart'),
    path('hx-menu-cart/', hx_menu_cart, name='hx_menu_cart'),
    path('hx-cart-total/', hx_cart_total, name='hx_cart_total'),
]