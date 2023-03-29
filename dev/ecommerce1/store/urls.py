from django.urls import path
from . import views


app_name = 'store'

urlpatterns = [
    path('', views.StoreView.as_view(), name='index'),
    path('product/<slug:slug>', views.ProductDetailView.as_view(), name='single'),
    path('search/<slug:slug>', views.ListCategoryView.as_view(), name='single_cat'),
]
