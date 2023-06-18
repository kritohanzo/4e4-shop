from django.shortcuts import render
from django.views import View
from core.decorators import confirm_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import AnonymousUser
from core.database_functions import get_all_objects, get_all_shoes, get_shoe, create_order, add_feedback
from .forms import BuyForm, FeedbackForm
import json
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
class ShopView(View):
    def get(self, request):
        template = 'shop/shop.html'
        objects = get_all_shoes()
        context = {"products": objects}
        return render(request, template, context)

class BuyView(View):
    @confirm_required
    def get(self, request):
        order_info = dict()
        order_info["product_id"] = request.GET.get('product-id')
        shoe = get_shoe(order_info["product_id"])[0]
        order_info["size"] = request.GET.get('product-size')
        order_info["quanity"] = request.GET.get('product-quanity')
        order_info["type_id"] = shoe.get('type_id')
        order_info["cost"] =  int(order_info["quanity"]) * int(shoe.get('selling_price_per_unit'))
        template = 'shop/buy.html'
        form = BuyForm(data={"product": order_info})
        context = {"form": form, "shoe": shoe, "order_info": order_info}
        return render(request, template, context)
    
    @confirm_required
    def post(self, request):
        client_info = dict()
        order_info = json.loads(request.POST.get('product').replace("'", '"'))
        client_info["full_name"] = request.POST.get('full_name')
        client_info["number"] = request.POST.get('number')
        client_info["mail_index"] = request.POST.get('mail_index')
        client_info["client_id"] = request.user.id
        shoe = get_shoe(order_info["product_id"])[0]
        order_ids = create_order(order_info, client_info)
        send_mail(f'Заказ(ы) с номером {" & ".join(list(map(str, order_ids)))}', message='123', from_email='test_smtp_timp@mail.ru', recipient_list=[f"{request.user.email}"], html_message=render_to_string('core/order_mail.html', {"client": client_info, "order": order_info, "shoe": shoe}))
        return redirect('shop:thanks_order')
    
class FeedbackView(View):
    def get(self, request):
        template = 'shop/feedback.html'
        form = FeedbackForm()
        context = {'form': form}
        return render(request, template, context)
    
    def post(self, request):
        feedback = request.POST.get('feedback')
        add_feedback(request.user.id, feedback)
        return redirect("shop:thanks_feedback")

class ThanksOrderView(View):
    def get(self, request):
        template = 'shop/thanks_order.html'
        return render(request, template)
    
class ThanksFeedbackView(View):
    def get(self, request):
        template = 'shop/thanks_feedback.html'
        return render(request, template)
