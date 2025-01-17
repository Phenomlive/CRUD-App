from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('products', views.product_list, name='products'),
    path('product/<int:pk>', views.product_detail, name='product_detail'),
    path('register', views.register, name='register')
]

urlpatterns = format_suffix_patterns(urlpatterns)
