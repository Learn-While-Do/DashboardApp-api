from django.urls import include, path
from rest_framework.routers import DefaultRouter
from reporting.views import CategoryViewSet, CustomerViewSet, OrderViewSet, ProductViewSet, SupplierViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet, basename='orders')
router.register('categories', CategoryViewSet, basename='categories')
router.register('customers', CustomerViewSet, basename='customers')
router.register('suppliers', SupplierViewSet, basename='suppliers')
router.register('products', ProductViewSet, basename='products')

urlpatterns = [

    path('', include(router.urls))
]