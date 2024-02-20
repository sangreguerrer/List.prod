from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    category = forms.ChoiceField(choices=Product.CategoryChoices.choices)

    class Meta:
        model = Product
        fields = ['title', 'description', 'quantity', 'category']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'quantity': 'Quantity',
            'category': 'Category',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
