from django.urls import path
from .views import *

app_name = 'books'

urlpatterns = [
    path('', home, name='home_view'),
    path('about/', about, name='about_view'),
    path('contact/', contact, name='contact_view'),
    path('book-list/', book_list, name='book_list'),
]
