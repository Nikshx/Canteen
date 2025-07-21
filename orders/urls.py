from django.urls import include, path
from .views import MenuItemList, OrderListCreateView, OrderDetailView
from . import views
urlpatterns = [
    path("menu-item/", MenuItemList.as_view(), name="menu-item-list"),
    path("menu-orders/", OrderListCreateView.as_view(), name="order-list-create"),
    path("menu-orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),

    path("", views.home, name='home'),

    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("register/", views.register, name="register"),
]
