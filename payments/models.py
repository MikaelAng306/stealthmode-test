from django.db import models

# Create your models here.
class Payment(models.Model):
    trxid = models.CharField(max_length=100, unique=True) ## Pour l'ID de la transaction
    montant = models.DecimalField(max_digits=10, decimal_places=2) ## Montant de la transaction
    monnaie = models.CharField(max_length=10, default='GHS') ## Pour le currncy de la monnaie
    email = models.EmailField(blank=True);
    status = models.CharField(max_length=50) ## Statut de la transaction
    created_at = models.DateTimeField(auto_now_add=True) ## Date d'initialisation de la transaction
    updated_at = models.DateTimeField(auto_now=True) ## Date de modification de la transaction