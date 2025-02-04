from django.contrib import admin


from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = [field.name for field in User._meta.fields]





@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Role._meta.fields]


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Permission._meta.fields]



@admin.register(LoginHistory)
class LoginHistoryAdmin(admin.ModelAdmin):
	list_display = [field.name for field in LoginHistory._meta.fields]



@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ActivityLog._meta.fields]


