from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'catalog_coins', CatalogCoinViewSet)


urlpatterns = router.urls
