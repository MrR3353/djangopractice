from time import strftime

from django.shortcuts import render
from .models import Order
from .forms import OrderForm

# Create your views here.
def first_page(request):
    order_list = Order.objects.all()
    form = OrderForm()
    return render(request, './index.html', {'order_list': order_list, 'form': form, 'load_time': strftime('%H:%M:%S')})

def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    order = Order(order_name=name, order_phone=phone)
    order.save()
    return render(request, './thanks_page.html', {'name': name, 'phone': phone})