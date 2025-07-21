from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuItem, Order
from .serializers import MenuItemSerializer, OrderSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

class MenuItemList(generics.ListCreateAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        return MenuItem.objects.filter(is_available=True)


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def login(request):
    return render(request, "login.html")

@login_required
def logout(request):
    return render(request, "logout.html")

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True  # ✅ silently set is_staff
            user.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})

def home(request):
    content = {'user': request.user}
    return render(request, "orders/index.html", content)
