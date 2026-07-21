from django import forms
from .models import ItemRequest

class ItemRequestForm(forms.ModelForm):
    class Meta:
        model = ItemRequest
        fields = ["message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 4, "placeholder": "Explain why you are interested in this item."})}
