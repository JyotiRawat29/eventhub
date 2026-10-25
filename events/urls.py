from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ReservationViewSet
from django.urls import path, include

# urlpatterns is a list of paths that the server will listen to

router = DefaultRouter()
router.register(r"events", EventViewSet, basename = 'event')
router.register(r"reservations", ReservationViewSet, basename = 'reservation')

urlpatterns = [
    path("",include(router.urls))
]