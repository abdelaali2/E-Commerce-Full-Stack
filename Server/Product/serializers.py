from rest_framework import serializers
from .models import Product
from Category.serializers import CategorySerializer
from Users.models import CustomUser
from shipments.serializers import ShipmentSerializer
from payments.serializers import PaymentsSerializer


class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField(read_only=True)
    dealer_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = (
            "categories",
            "name",
            "description",
            "quantity",
            "id",
            "dealer",
            "dealer_name",
            "price",
            "discount",
        )

    def get_categories(self, obj):
        categories = obj.category.all()
        serialized_categories = CategorySerializer(categories, many=True).data
        return serialized_categories

    def get_dealer_name(self, obj):
        user = CustomUser.objects.get(pk=obj.dealer.id)
        return user.username
