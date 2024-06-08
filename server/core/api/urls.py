from django.urls import path, include
from .views import AppsConfig
from .api_router import router

urlpatterns = [
    path('', include(router.urls)),
    path('apps-config/', AppsConfig.as_view(), name='apps-config'),
]