from django.db import models
from accounts.models import UserProfile  # if you’re linking to actual users
from common.models import ArchiveMixin, ActiveManager

class Transaction(ArchiveMixin):
    code = models.CharField(max_length=25, blank=True, null=True)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)
    is_posted = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    invoice = models.CharField(max_length=50, blank=True, null=True)

    objects = ActiveManager()      # Default manager: shows only active records
    all_objects = models.Manager() # Backup manager: shows everything

    def __str__(self):
        return f"Transaction {self.id} - {self.status or 'Pending'}"