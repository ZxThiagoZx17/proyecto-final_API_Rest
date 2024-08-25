from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, CategoryViewSet, UserViewSet

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
