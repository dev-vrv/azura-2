from django.db import models

class Mails(models.Model):
    recipients = models.JSONField(default=list)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivered_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'mails'
        verbose_name = 'Mail'
        verbose_name_plural = 'Mails'

    def __str__(self):
        return self.subject