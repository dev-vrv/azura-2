from api.next_admin import NextAdminController
from .models import Mails
from .serializers import MailsAdminSerializer

class MailsAdminController(NextAdminController):
    model = Mails
    serializer_class = MailsAdminSerializer