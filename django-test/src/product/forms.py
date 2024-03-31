from django import forms
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput
from product.models import Variant, Product


class VariantForm(ModelForm):
    class Meta:
        model = Variant
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'active'})
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'sku': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
        }


class ProductFilterForm(forms.Form):
    title = forms.CharField(required=False)
    variant = forms.ModelChoiceField(queryset=Variant.objects.filter(active=True), required=False)
    price_from = forms.DecimalField(required=False)
    price_to = forms.DecimalField(required=False)
    date_from = forms.DateField(required=False)
    date_to = forms.DateField(required=False)