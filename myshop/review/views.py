from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Product
from .models import Review
from .forms import ReviewForm


# чтобы отзыв работал на странице товара нужно добавить в шаблон product_detail.html
# нужно добавить в shop.views

@login_required   
#декоратор чтобы отзыв мог оставить только авторизованный пользователь
# можно протестировать отзывы просто убрать декоратор  @login_required  
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Проверяем, оставлял ли уже этот пользователь отзыв на этот продукт 
    existing_review = Review.objects.filter(product=product, user=request.user).first()
    if existing_review:
        # Выводим сообщение на той же странице
        return render(request, 'shop/product/detail.html', {
            'product': product,
            'review_form': ReviewForm(),
            'error_message': "Вы уже оставили отзыв для этого товара.",
        })
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('shop:product_detail', id=product.id, slug=product.slug)
    return redirect('shop:product_detail', id=product.id, slug=product.slug)
#для проверки авторизации тестировать
    # if request.method == 'POST':
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         review = form.save(commit=False)
    #         review.product = product

    #         # Если есть залогиненный пользователь, ставим его, иначе None
    #         if request.user.is_authenticated:
    #             review.user = request.user
    #         else:
    #             review.user = None

    #         review.save()
    #         return redirect('shop:product_detail', id=product.id, slug=product.slug)

    # return redirect('shop:product_detail', id=product.id, slug=product.slug)