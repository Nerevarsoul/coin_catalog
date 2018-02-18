from django.db import models


class ErrorMixin(models.Model):
    class Meta:
        abstract = True

    error_message = models.CharField(max_length=250)
    error_code = models.CharField(max_length=10)

    def error(self, msg, code=None):
        self.error_message = msg
        self.error_code = code
        self.save(update_fields=['error_message', 'error_code', 'modified'])
