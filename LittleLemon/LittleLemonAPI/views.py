from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer, UserSerializer
from django.contrib.auth.models import Group, User
from rest_framework.decorators import action
from rest_framework.response import Response

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, methods=['post'])
    def assign_group(self, request, pk=None):
        user = self.get_object()
        group_name = request.data.get('group')
        group = Group.objects.get(name=group_name)
        user.groups.add(group)
        return Response({'status': 'user added to group'})
