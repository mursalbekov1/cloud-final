from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    UserViewSet, EventViewSet, RegistrationViewSet, NotificationViewSet,
    PaymentViewSet, VenueViewSet, TicketViewSet, ReviewViewSet,
    CategoryViewSet, EventCategoryViewSet
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Cloud API",
        default_version='v1',
        description="API documentation",
        license=openapi.License(name="Cloud License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'events', EventViewSet)
router.register(r'registrations', RegistrationViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'venues', VenueViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'eventcategories', EventCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
