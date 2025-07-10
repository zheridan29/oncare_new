from django.db import models
from accounts.models import UserProfile  # assuming you have this model defined in accounts app
from common.models import ArchiveMixin, ActiveManager


class Product(ArchiveMixin):
    name = models.CharField(max_length=255)
    medicine_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    quantity = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    
    created_by = models.CharField(max_length=25, blank=True, null=True)  # or link to UserProfile later
    is_deleted = models.BooleanField(default=False)

    objects = ActiveManager()      # Default manager: shows only active records
    all_objects = models.Manager() # Backup manager: shows everything

    def __str__(self):
        return self.name
    

class StockEntry(ArchiveMixin):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    stock_date = models.DateField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)

    objects = ActiveManager()      # Default manager: shows only active records
    all_objects = models.Manager() # Backup manager: shows everything

    def __str__(self):
        return f"Stock entry for {self.product} on {self.stock_date}"