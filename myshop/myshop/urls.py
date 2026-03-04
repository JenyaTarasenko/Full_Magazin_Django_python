
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),  #приложение cart   
    path('orders/', include('orders.urls', namespace='orders')), #приложение orders 
    path('', include('shop.urls', namespace='shop')),  #приложение shop
    path('reviews/', include('review.urls', namespace='review')), # Отзывы
    path('accounts/', include('accounts.urls', namespace='accounts')), # Аккаунты
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
