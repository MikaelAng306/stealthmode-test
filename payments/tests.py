# from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.
class Tests(APITestCase):
    def init_payment_with_email(self):
        data = {
            "montant": "5000",
            "email": "mikaelanago306@gmail.com",
        }
        response = self.client.post("/payments/initiate/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def init_payment_without_email(self):
        data = {
            "montant": "5000",
        }
        response = self.client.post("/payments/initiate/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def init_payment_without_amount(self):
        data = {
            "email": "mikaelanago306@gmail.com",
        }
        response = self.client.post("/payments/initiate/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    def test_payments_track(self):
        response = self.client.get("/payments/verify/?transaction_id=77")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

