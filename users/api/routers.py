from rest_framework.routers import DefaultRouter
from .views import UserApiViewSet

router_users = DefaultRouter()
router_users.register(prefix='users/', basename='users',
                      viewset=UserApiViewSet)
