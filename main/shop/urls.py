from django.urls import path
from .views import ShopView, BuyView, FeedbackView, ThanksOrderView, ThanksFeedbackView
from django.contrib.auth.decorators import login_required
from core.decorators import worker_required

app_name = 'shop'

urlpatterns = [
    path('', (ShopView.as_view()), name='index'),
    path('buy/', login_required(BuyView.as_view()), name='buy'),
    path('feedback/', login_required(FeedbackView.as_view()), name='feedback'),
    path('thanks_order/', login_required(ThanksOrderView.as_view()), name='thanks_order'),
    path('thanks_feedback/', login_required(ThanksFeedbackView.as_view()), name='thanks_feedback'),
]