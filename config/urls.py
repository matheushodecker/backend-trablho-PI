from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from order.views import CustomerViewSet, OrderViewSet, OrderItemViewSet

router = DefaultRouter()

router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitems', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]