from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
# from .tasks import order_created
from cart.cart import Cart
from django.views.decorators.csrf import csrf_exempt
from .services import get_liqpay_context
from .telegram_bot import send_telegram_message

def payment_success(request):
    #страница успеха оплаты 
    return render(request, 'orders/order/payment_success.html')


def payment_cancel(request):
    #страница отмены оплаты
    return render(request, 'orders/order/payment_cancel.html')


@csrf_exempt # LiqPay присылает POST-запрос без нашего CSRF-токена
def liqpay_webhook(request):
    print("WEBHOOK CALLED")
    liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
    data = request.POST.get('data')
    signature = request.POST.get('signature')
    
    # Проверяем подпись, чтобы никто не подделал ответ
    sign = liqpay.str_to_sign(settings.LIQPAY_PRIVATE_KEY + data + settings.LIQPAY_PRIVATE_KEY)
    
    if sign == signature:
        response = liqpay.decode_data_from_str(data)
        # Если статус 'success' или 'wait_accept' (деньги в обработке)
        if response['status'] in ['success', 'wait_accept']:
            order_id = response['order_id']
            order = Order.objects.get(id=order_id)
            order.paid = True
            order.save()
            # 🔥 Формируем красивое сообщение
            message = f"""
                ✅ <b>Новый оплаченный заказ!</b>

                📦 Заказ №{order.id}
                👤 Имя: {order.first_name} {order.last_name}
                📧 Email: {order.email}
                💰 Сумма: {order.get_total_cost()} UAH
                """

            send_telegram_message(message)
            
    return HttpResponse()

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # Получаем данные для кнопки LiqPay
            res = get_liqpay_context(order)
            print(f"DEBUG DATA: {res}")
            return render(request,
                          'orders/order/created.html',
                          {'order': order, 'liqpay': res})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})