from django.conf import settings
from django.db import models
from shop.models import Product

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField("Отзыв")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        unique_together = ('product', 'user')  # 1 отзыв на товар от 1 пользователя

    def __str__(self):
        return f"{self.user.email} - {self.product.name}"