from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.forms import ValidationError

from django_currentuser.middleware import (get_current_authenticated_user, get_current_user)

from authentication.models import *

User = get_user_model()


def created_by_signals(sender, instance, created, **kwargs):
	if created:
		user = get_current_authenticated_user()
		if user is not None:
			sender.objects.filter(id=instance.id).update(created_by=user)


def updated_by_signals(sender, instance, created, **kwargs):
	if not created:
		user = get_current_authenticated_user()
		if user is not None:
			sender.objects.filter(id=instance.id).update(updated_by=user)





def activity_by_signals(sender, instance, created, **kwargs):
	if created:
		user = get_current_authenticated_user()
		if user is not None:
			sender.objects.filter(id=instance.id).update(activity_by=user)



# Permission signals
post_save.connect(created_by_signals, sender=Permission)
post_save.connect(updated_by_signals, sender=Permission)


# Role signals
post_save.connect(created_by_signals, sender=Role)
post_save.connect(updated_by_signals, sender=Role)


# User signals
post_save.connect(created_by_signals, sender=User)
post_save.connect(updated_by_signals, sender=User)

# LoginHistory signals
post_save.connect(created_by_signals, sender=LoginHistory)
post_save.connect(updated_by_signals, sender=LoginHistory)



