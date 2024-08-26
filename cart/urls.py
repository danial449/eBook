# urls.py

from django.urls import path
from .views import add_to_cart, view_cart, update_cart_item

urlpatterns = [
    path('cart/add/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/update/<int:item_id>/', update_cart_item, name='update_cart_item'),
]
