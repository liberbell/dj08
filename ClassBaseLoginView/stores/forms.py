from django import forms

class CartUpdateForm(forms.ModelForm):

    class Meta:
        model = CartItems