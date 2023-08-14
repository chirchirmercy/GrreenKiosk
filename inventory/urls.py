from django.urls import path
from .views import product_detail
from .views import product_upload_view
from .views import products_list
from .views import product_update_view
from . import views

urlpatterns=[
    path("products/upload/",product_upload_view,name="product_upload_view"),
    path("products/list/",products_list,name="products_list"),
    path("products/<int:id>/",product_detail,name="product_detail_view"),
    path("products/edit/<int:id>/" , product_update_view,name='product_update_view'),
    # urls.py


    path("add_to_cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    
]

    
    




