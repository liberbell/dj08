from django import forms
from .models import CartItems

class CartUpdateForm(forms.ModelForm):
    quantity = forms.IntegerField()
    id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = CartItems
        fields = ["quantity", "id"]