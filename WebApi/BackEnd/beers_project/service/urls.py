from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Beer', views.BeerViewSet)
router.register(r'Users', views.UsersViewSet)
router.register(r'Kind', views.KindViewSet)
router.register(r'Selection', views.SelectionViewSet)
router.register(r'UpTake', views.UpTakeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
