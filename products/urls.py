from django.urls import path
from .views import *
urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]