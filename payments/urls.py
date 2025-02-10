from django.urls import path
from .views import PaymentInitView, PaymentTrackView

urlpatterns = [
    path('initiate/', PaymentInitView.as_view(), name='payment_init'),
    path('verify/', PaymentTrackView.as_view(), name='payment_track'),
]

