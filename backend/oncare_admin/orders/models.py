from django.db import models
from inventory.models import Product
from accounts.models import UserProfile
from common.models import ArchiveMixin, ActiveManager

class Order(ArchiveMixin):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    
    ordered_quantity = models.IntegerField(null=True, blank=True)
    served_quantity = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)
    code = models.CharField(max_length=25, null=True, blank=True)
    date_ordered = models.DateTimeField(null=True, blank=True)
    is_saved = models.BooleanField(default=False)

    objects = ActiveManager()      # Default manager: shows only active records
    all_objects = models.Manager() # Backup manager: shows everything

    def __str__(self):
        return f"Order #{self.id} by {self.user.username if self.user else 'Guest'}"