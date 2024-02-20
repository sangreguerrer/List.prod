from django.urls import path

from .views import (
    product_list,
    add_product,
    ProductDeleteView,
    index, show_product,
    ProductUpdate
)

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_product, name='add_product'),
    path('product_list/', product_list, name='product_list'),
    path('product_list/<slug:slug>/', show_product, name='product'),
    path(
        'product_list/<int:id>/edit/',
        ProductUpdate.as_view(),
        name='update_product'
    ),
    path(
        'product_list/<int:pk>/delete/',
        ProductDeleteView.as_view(),
        name='delete'),
]
