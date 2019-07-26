from rest_framework import routers

from .views import UserViewSet, MainViewSet


router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('main', MainViewSet)


urlpatterns = [

]

urlpatterns += router.urls