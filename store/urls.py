from django.urls import path
from . import views
from .views import ProfileCreateView

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart),
    path('products/', views.products_list_view, name='products_list'),
    path('products/<int:id>', views.products_detail, name='products_detail'),
    path('checkout/', views.checkout),
    path('sign-up/', views.sign_up_view, name='sign_up'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/create/', ProfileCreateView.as_view(), name='profile_create')
]
