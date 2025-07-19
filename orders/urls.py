from django.urls import include, path
from .views import MenuItemList, OrderListCreateView, OrderDetailView
urlpatterns = [
    path("menu-item/", MenuItemList.as_view(), name='menu-item-list'),
    path('menu-orders/', OrderListCreateView.as_view(),name='order-list-create'), 
    path('menu-orders/<int:pk>/', OrderDetailView.as_view(),name='order-detail'),
    
    
]
