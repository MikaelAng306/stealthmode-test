from django.shortcuts import render
from rest_framework.views import APIView
import requests
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import Payment

paystackapi_key = getattr(settings, 'PAYSTACK_SECRET_KEY')

base_url = "https://api.paystack.co"
headers = {
            "Authorization": f"Bearer {paystackapi_key}",
            "Content-Type": "application/json",
        }

# Create your views here.
class PaymentInitView(APIView):
    def post(self, request):
        data = request.data
        montant = data.get('montant')
        monnaie = data.get('monnaie', 'GHS')
        email = data.get('email')
        
        if not montant:
            return Response({"error: Invalid amount"}, status=status.HTTP_400_BAD_REQUEST)
        
        to_send = {
            "amount": int(float(montant) * 100), ##Sending an amount in subunits simply means multiplying the base amount by 100. For example, if a customer is supposed to make a payment of NGN 100, you would send 10000 = 100 * 100 in your request.
            "email": email,
            "currency": monnaie,
        }
        response = requests.post(base_url + "/transaction/initialize", json=to_send, headers=headers)
        if response.status_code == 200:
            result = response.json()
            trxid = result.get('data', {}).get('reference')
            Payment.objects.create(
                trxid = trxid,
                montant = montant,
                monnaie = monnaie,
                email = email,
                status="true",
            )
            return Response(result, status=status.HTTP_200_OK)

        return Response(response.json(), status=response.status_code)

class PaymentTrackView(APIView):
    def get(self, request):
        trxid = request.query_params.get('transaction_id')
        
        if not trxid:
            return Response({"ID de la transaction non specifie"}, status=status.HTTP_400_BAD_REQUEST)
        
        url = base_url + f"/transaction/verify/{trxid}"
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            payment = Payment.objects.filter(trxid=trxid).first()
            if not payment:
                return Response({"error: Not found in database"}, status=status.HTTP_409_CONFLICT)
            else:
                payment.save()
            return Response(result, status=status.HTTP_200_OK)
        return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)