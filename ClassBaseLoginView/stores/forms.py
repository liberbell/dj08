from django import forms
from .models import CartItems, Addresses
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

class CartUpdateForm(forms.ModelForm):
    quantity = forms.IntegerField(label="stock", min_value=1)
    id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = CartItems
        fields = ["quantity", "id"]

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get("quantity")
        id = cleaned_data.get("id")
        cart_item = get_object_or_404(CartItems, pk=id)
        if quantity > cart_item.product.stock:
            raise ValidationError(f"Over the stock. Input under {cart_item.product.stock}.")
        
class AddressInputForm(forms.ModelForm):
    address = forms.CharField(label="Address", widget=forms.TextInput(attrs={"size":"80"}))

    class Meta:
        model = Addresses
        fields = ["zip_code", "prefecture", "address"]
        labels = {
            "zip_code": "Zip Code",
            "prefecture": "Prefecture",
        }

    def save(self):
        address = super().save(commit=False)
        address.user = self.user
        address.save()
        return address 