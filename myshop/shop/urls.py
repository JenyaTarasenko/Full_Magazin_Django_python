# shop/urls.py
from django.urls import path
from . import views

app_name = 'shop'

# templates/ shop/
#           base.html 
#           product/
#               list.html 
#               detail.html 

urlpatterns = [
    #поиск должен быть выше чтобы он мог работать 
    # поиск продуктов shop/product/search_results.html
    path('search/', views.search_products, name='search'),
    path('', views.product_list, name='product_list'), 
    path('<slug:category_slug>/', views.product_list,name='product_list_by_category'), 
    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
   
]