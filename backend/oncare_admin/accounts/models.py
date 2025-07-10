from django.db import models
from common.models import ArchiveMixin, ActiveManager

class UserProfile(ArchiveMixin):
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=128)  # for hashed passwords
    user_type = models.CharField(max_length=15)  # e.g. 'admin', 'customer', etc.

    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    email = models.EmailField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)

    is_active = models.BooleanField(default=False)
    status = models.CharField(max_length=7, blank=True, null=True)
    date_registered = models.DateTimeField(null=True, blank=True)

    objects = ActiveManager()      # Default manager: shows only active records
    all_objects = models.Manager() # Backup manager: shows everything


    def __str__(self):
        return f"{self.username} ({self.user_type})"