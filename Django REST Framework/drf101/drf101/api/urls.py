from django.urls import path

from drf101.api.views import ManualProductsListView, ProductsListViews, SingleProductView

urlpatterns = [
    path('products-manual/', ManualProductsListView.as_view(), name='products list'),
    path('products/', ProductsListViews.as_view(), name='products list'),
    path('products/<int:pk>', SingleProductView.as_view(), name='single product'),
]
