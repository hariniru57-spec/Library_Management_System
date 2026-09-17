from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate(self, data):
        quantity = data.get("quantity", getattr(self.instance, "quantity", None))
        available = data.get("available_quantity", getattr(self.instance, "available_quantity", None))
        if quantity is not None and available is not None and available > quantity:
            raise serializers.ValidationError({"available_quantity": "Cannot exceed total quantity."})
        return data
