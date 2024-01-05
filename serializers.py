# affinity_api/serializers.py
from rest_framework import serializers
from .models import Item, Transaction

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        transaction = Transaction.objects.create(**validated_data)

        for item_data in items_data:
            Item.objects.create(transaction=transaction, **item_data)

        return transaction
