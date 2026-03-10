from django.contrib import admin
from .models import Category, Product, Slider, SliderImage



# категории продуктов
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    # Автоматически заполняет slug из поля name
    prepopulated_fields = {'slug': ('name',)}

# Продукты
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'available'] # Можно менять цену прямо в списке!
    prepopulated_fields = {'slug': ('name',)}

# Слайдер
class SliderImageInline(admin.TabularInline):
    model = SliderImage
    extra = 5   # можно добавить до 5 картинок


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):

    list_display = ("title", "active")

    list_filter = ("active",)

    inlines = [SliderImageInline]
