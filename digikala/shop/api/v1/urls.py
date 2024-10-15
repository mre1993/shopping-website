from django.urls import path
from .views import product_list_api_view, product_detail_api_view

urlpatterns = [
    path("", product_list_api_view, name="products_api"),
    path("product/<int:pk>/", product_detail_api_view, name="product_api"),
]
