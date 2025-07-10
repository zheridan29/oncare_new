from django.db import models
from inventory.models import Product
from accounts.models import UserProfile  # or you can use CharField if not linking yet
from common.models import ArchiveMixin, ActiveManager

class ProductAudit(ArchiveMixin):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(null=True, blank=True)
    performed_by = models.CharField(max_length=25, blank=True, null=True)  # or ForeignKey to UserProfile
    action = models.CharField(max_length=50, blank=True, null=True)
    
    new_quantity = models.IntegerField(blank=True, null=True)
    old_quantity = models.IntegerField(blank=True, null=True)
    new_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    objects = ActiveManager()      # Default manager: shows only active records
    all_objects = models.Manager() # Backup manager: shows everything

    def __str__(self):
        return f"Audit #{self.id} - {self.action} on {self.product}"