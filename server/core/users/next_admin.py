from api.next_admin import NextAdminController
from .models import User
from .serializers import UserAdminSerializer


class UserAdminController(NextAdminController):
    model = User
    serializer_class = UserAdminSerializer