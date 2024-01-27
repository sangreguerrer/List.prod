from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DeleteView
from .filters import CategoryFilter
from .forms import ProductForm
from .models import Product
from django_filters.views import FilterMixin


def index(request):
    template = 'base.html'
    context = request
    return render(request, template)


def product_list(request):
    catfilter = CategoryFilter(request.GET, queryset=Product.objects.all())
    sort = request.GET.get('sort')
    if sort == 'title':
        products = catfilter.qs.order_by('title')
    elif sort == 'min_quantity':
        products = catfilter.qs.order_by('quantity')
    elif sort == 'max_quantity':
        products = catfilter.qs.order_by('-quantity')
    else:
        products = catfilter.qs
    return render(request, 'product_list.html', {'form': catfilter.form, 'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def show_product(request, slug):
    template = 'product.html'
    product = Product.objects.filter(slug__contains=slug).first()
    context = {'product': product}
    return render(request, template, context)


class ProductUpdate(FilterMixin, UpdateView):
    model = Product
    fields = ['title', 'description', 'quantity']
    form = ProductForm()
    template_name = 'update_product.html'
    pk_url_kwarg = 'id'

    def get_absolute_url(self):
        return reverse('product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Product.objects.all()
        context['filter'] = CategoryFilter(self.request.GET, queryset=queryset)
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = reverse_lazy('product_list')