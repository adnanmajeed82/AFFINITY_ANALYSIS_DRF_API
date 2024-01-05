# affinity_api/models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    #transaction = models.ForeignKey('Transaction', related_name='items', on_delete=models.CASCADE)

class Transaction(models.Model):
    items = models.ManyToManyField(Item)
    timestamp = models.DateTimeField(auto_now_add=True)
