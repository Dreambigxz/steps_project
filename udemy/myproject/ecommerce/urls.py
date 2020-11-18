from . import views, category_views
from django.urls import path


urlpatterns= [

    path('', views.HomeListView.as_view(), name='product_store'),
    path('products/', views.ProductDetailView.as_view(), name='product'),
    path('sports/', category_views.SportCartigoryListView.as_view(), name='sports'),
]