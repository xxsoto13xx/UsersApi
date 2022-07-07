from importlib.resources import path
from rest_framework import routers
from users.api.views import UserApiViewSet

router = routers.SimpleRouter()
router.register('', UserApiViewSet, basename='users')
urlpatterns = router.urls
