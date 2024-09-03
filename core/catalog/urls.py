from django.urls import path

from core.catalog.views import *


urlpatterns = [
    path('', CatalogView.as_view(), name='CatalogView'),
    path('<int:id_producto>/detail_product', optenerProducto, name='detail_product'),
    path('ver_carrito/', ver_carrito, name='ver_carrito'),
    path('vaciar_carrito/', vaciar_carrito, name='vaciar_carrito'),
    path('eliminarProducto/<int:id_producto>', eliminarProducto, name='eliminarProducto'),
    path('shear_product/',shear_product, name='shear_product'),
    path('<int:id_categoria>/mostrar_por_categoria', mostrar_por_categoria, name='mostrar_por_categoria'),
    path('confirmar_compra/', confirmar_compra, name='confirmar_compra'),
]