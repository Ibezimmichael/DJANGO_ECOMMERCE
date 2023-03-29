from django.shortcuts import render
from .models import Category, Product
from django.views.generic import TemplateView, DetailView, ListView, DeleteView, CreateView
from django.shortcuts import get_object_or_404
# Create your views here.

class StoreView(ListView):
    model = Product
    template_name = 'store/store.html'


def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}

    
class ListCategoryView(ListView):
    def get(self, request, slug=None):
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=category)
        context = {'category': category, 'products': products}
        return render(request, 'store/single_category_list.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'
    