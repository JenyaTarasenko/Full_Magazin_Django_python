from django.db import models
from django.urls import reverse # Для генерации ссылок

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL (слаг)")

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Это позволит Django самому находить путь к категории
        # Предполагаем, что в urls.py имя пути 'catalog:product_list_by_category'
        return reverse('catalog:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True) 
    description = models.TextField(blank=True) 
    price = models.DecimalField(max_digits=10,decimal_places=2) 
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['name']
        indexes = [
        models.Index(fields=['id', 'slug']), 
        models.Index(fields=['name']), models.Index(fields=['-created']),]

    def __str__(self): 
        return self.name

    # метод для получения ссылки на продукт
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    

