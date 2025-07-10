# common/models.py
from django.db import models

class ArchiveMixin(models.Model):
    is_archived = models.BooleanField(default=False)

    class Meta:
        abstract = True

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_archived=False)
