from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from review.forms import ReviewForm  #форма отзыва
from django.db.models import Q




def about(request):
    return render(request, "pages/about.html")

def contacts(request):
    return render(request, "pages/contacts.html")



# все продукты выводится в шаблон списком 
def product_list(request, category_slug=None): 
    category = None
    # категории товара вывод на главной странице 
    categories = Category.objects.all()
    # все продукты вывод на главной странице 
    products = Product.objects.filter(available=True) 
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category) 
    return render(request,'shop/product/product_list.html', {'category': category, 'categories': categories, 'products': products})

# вывод одного продукта
def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    #форма отзыва прилетела из myshop.review/forms.py
    review_form = ReviewForm()
    return render(request, 'shop/product/detail.html',{'product': product, 'cart_product_form': cart_product_form, 'review_form': review_form})


# поиск продуктов shop/product/search_results.html
# поиск работает по name, description, category__name можно также сделать по бренду 
def search_products(request):
    query = request.GET.get('q', '')
    results = Product.objects.filter( Q(name__icontains=query) |
                                        Q(description__icontains=query) |
                                        Q(category__name__icontains=query) 
                                        # Q(brand__name__icontains=query)
                                    ).distinct() if query else Product.objects.none()
    
    return render(request, 'include/search_results.html', {
        'results': results,
        'query': query
    })