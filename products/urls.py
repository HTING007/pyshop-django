from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='home'),
    path('products/<int:id>/', views.detail, name='product_detail'),
    path('new', views.new, name='new_product')
]