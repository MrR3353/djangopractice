from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendmessages import send_message


def first_page(request):
    slider_list = CmsSlider.objects.all()
    price_cards = PriceCard.objects.all()[:3]
    price_tables = PriceTable.objects.all()
    form = OrderForm()
    return render(request, './index.html', {'slider_list': slider_list,
                                            'price_cards': price_cards,
                                            'price_tables': price_tables,
                                            'form': form})


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        order = Order(order_name=name, order_phone=phone)
        order.save()
        send_message(name, phone)
        return render(request, './thanks.html', {'name': name, 'phone': phone})
    return render(request, './thanks.html')

