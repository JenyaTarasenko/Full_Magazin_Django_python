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
    # главная страница формируется весь урл главной не как в реакт все в месте через функции
    path('', views.product_list, name='product_list'), 
    # about
    path('about/', views.about, name='about'),
    # contacts
    path('contacts/', views.contacts, name='contacts'),
    # продукты
    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
        # категории
    path('<slug:category_slug>/', views.product_list,name='product_list_by_category'), 
   
]