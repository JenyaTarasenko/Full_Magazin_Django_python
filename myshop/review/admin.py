from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'text_short', 'created')
    list_filter = ('created', 'product')
    search_fields = ('user__username', 'user__email', 'text', 'product__name')
    readonly_fields = ('user', 'created')  # запрет редактирования пользователя и даты

    def text_short(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_short.short_description = 'Отзыв'