
from django.db import models
import uuid

from django.utils import timezone
from commons.managers import SoftDeleteManager

class BaseModel(models.Model):
 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=False, null=True, blank=True)

    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class SoftDeleteModel(BaseModel):
    """Abstract model for soft-deletable objects."""
    is_deleted = models.BooleanField(default=False)  
  

    # Managers
    active_objects = SoftDeleteManager() 
    all_objects = models.Manager() 

    def soft_delete(self, *args, **kwargs):
        """Soft delete function for model instance."""
        self.is_deleted = True
        self.deleted_at = timezone.now() 
        self.save()

    def restore(self, *args, **kwargs):
        """Restore a soft-deleted model instance."""
        self.is_deleted = False
        self.deleted_at = None  
        self.save()

    def permanent_delete(self, *args, **kwargs):
        """Permanently delete a model object instance."""
        super().delete(*args, **kwargs)

    class Meta:
        abstract = True
