from django import forms
from .models import CartItems
from django.shortcuts import get_object_or_404

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
            
        return data
        