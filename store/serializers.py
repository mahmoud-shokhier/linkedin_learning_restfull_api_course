from rest_framework import serializers

from store.models import Product, ShoppingCartItem

class CartItemSerialzer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=200)
    
    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'quantity')
        
class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description= serializers.CharField(max_length=200, min_length=2)
    cart_items = serializers.SerializerMethodField()
    # price = serializers.FloatField(min_value=1, max_value=100)
    price = serializers.DecimalField(min_value=1, max_value=10000, max_digits=None, decimal_places=2)
    sale_start = serializers.DateField(
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True, 
        help_text="Accepted format is '12:01 PM 28 July 2022'",
        style={'input_type': 'text', 'placeholder': '12:01 PM 28 July 2022'}
    )
    sale_end = serializers.DateField(
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True, 
        help_text="Accepted format is '12:01 PM 28 July 2022'",
        style={'input_type': 'text', 'placeholder': '12:01 PM 28 July 2022'}
    )
    # photo = serializers.ImageField(default=None,allow_null=True, required=False,)
    warranty = serializers.FileField(write_only=True, default=None, required=False,)
    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'sale_start', 'sale_end', 'is_on_sale', 'current_price', 'cart_items', 'warranty',
            )

    def get_cart_items(self, instance):
        items = ShoppingCartItem.objects.filter(product=instance)
        return CartItemSerialzer(items, many=True).data
    
    def update(self, instance,validated_data):
        if validated_data.get('warranty', None):
            instance.description =  '\n\nWarranty information: \n'
            instance.description += b'; '.join(
                validated_data['warranty'].readlines()
            ).decode()
        return instance
    
    def create(self, validated_data):
        validated_data.pop('warranty')
        return Product.objects.create(**validated_data)
        
class ProductStatSerializer(serializers.Serializer):
    stats = serializers.DictField(
        child = serializers.ListField(
            child=serializers.IntegerField()
        )
    )
