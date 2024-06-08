from rest_framework.routers import DefaultRouter
from users.next_admin import UserAdminController

router = DefaultRouter()
router.register(r'users', UserAdminController, basename='Users')

urls = router.urls