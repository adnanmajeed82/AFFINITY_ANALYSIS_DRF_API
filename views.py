# affinity_api/views.py
from rest_framework import viewsets
from .models import Item, Transaction
from .serializers import ItemSerializer, TransactionSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from efficient_apriori import apriori

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=False, methods=['get'])
    def perform_affinity_analysis(self, request):
        transactions = Transaction.objects.values_list('items__name', flat=True)
        transactions = [set(items) for items in transactions]

        itemsets, rules = apriori(transactions, min_support=0.2, min_confidence=0.5)

        return Response({'itemsets': itemsets, 'rules': rules})
