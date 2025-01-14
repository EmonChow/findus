
from django.db import models

class SoftDeleteManager(models.Manager):
    """Soft Delete manager"""
    
    def get_queryset(self):
        """Returns the queryset excluding soft-deleted objects."""
        return super().get_queryset().filter(is_deleted=False, deleted_at__isnull=True)
