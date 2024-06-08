from rest_framework.routers import DefaultRouter
from users.next_admin import UserAdminController
from mails.next_admin import MailsAdminController

router = DefaultRouter()
router.register(r'users', UserAdminController, basename='Users')
router.register(r'mails', MailsAdminController, basename='Mails')

urls = router.urls