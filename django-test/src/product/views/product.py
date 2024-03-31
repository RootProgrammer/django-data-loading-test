from django.shortcuts import redirect, render
from django.views import generic

from product.models import Variant, Product
from product.forms import ProductFilterForm, ProductForm


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        context['product_form'] = ProductForm()
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

    def post(self, request, *args, **kwargs):
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('list.product')
        else:
            # If the form is not valid, re-render the page with the form errors.
            context = self.get_context_data()
            context['product_form'] = product_form  # Pass the form back to the template with errors
            return render(request, self.template_name, context)


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 7
    template_name = 'products/list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filter_form = ProductFilterForm(self.request.GET)
        if self.filter_form.is_valid():
            if self.filter_form.cleaned_data.get('title'):
                queryset = queryset.filter(title__icontains=self.filter_form.cleaned_data['title'])
            if self.filter_form.cleaned_data.get('variant'):
                queryset = queryset.filter(variants=self.filter_form.cleaned_data['variant'])
            if self.filter_form.cleaned_data.get('price_from'):
                queryset = queryset.filter(productvariantprice__price__gte=self.filter_form.cleaned_data['price_from'])
            if self.filter_form.cleaned_data.get('price_to'):
                queryset = queryset.filter(productvariantprice__price__lte=self.filter_form.cleaned_data['price_to'])
            if self.filter_form.cleaned_data.get('date_from'):
                queryset = queryset.filter(created_at__gte=self.filter_form.cleaned_data['date_from'])
            if self.filter_form.cleaned_data.get('date_to'):
                queryset = queryset.filter(created_at__lte=self.filter_form.cleaned_data['date_to'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.filter_form or ProductFilterForm()
        return context
