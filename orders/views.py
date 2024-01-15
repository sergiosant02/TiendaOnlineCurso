from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from orders.models import Order, OrderLine
from shopcart.cart import Cart
from shop.models import Product
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
# Create your views here.

@login_required(login_url="/authentication/login")
def process_order(request):
    order = Order.objects.create(user=request.user)
    cart = Cart(request=request)
    order_lines = list()
    for key, value in cart.cart.items():
        product = Product.objects.get(id=value["product_id"])
        order_lines.append(OrderLine(
            product=product,
            quantity=value["quantity"],
            user=request.user,
            order=order
        ))
    OrderLine.objects.bulk_create(order_lines)
    send_mail_order(order = order, order_lines = order_lines, username = request.user.username)
    messages.success(request, "Pedido realizado correctamente")
    return redirect("shop")
    
    
def send_mail_order(**kwargs):
    subject = "Gracias por el pedido"
    message = render_to_string("emails/order.html", {
        "order": kwargs.get("order"),
        "order_lines": kwargs.get("order_lines"),
        "username": kwargs.get("username")
        })
    message_txt = strip_tags(message)
    from_email = "decide202324@gmail.com"
    to_email = "sergiosantiago0403@gmail.com"
    
    send_mail(subject, message_txt, from_email, [to_email], html_message=message)