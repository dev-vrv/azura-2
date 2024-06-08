from api.serializers import NextAdminSerializer
from .models import Mails

class MailAdminSerializer(NextAdminSerializer):
    class Meta:
        model = Mails
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')