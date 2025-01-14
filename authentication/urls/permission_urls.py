
from django.urls import path
from authentication.views import permission_views as views


urlpatterns = [
	path('all/', views.getAllPermission),

	path('without_pagination/all/', views.getAllPermissionWithoutPagination),

	path('get_all_permission_by_user_role/', views.getAllPermissionByUserRole),

	path('check_permission_by_user/', views.checkPermissionByUser),

	path('<int:pk>', views.getAPermission),

	path('search/', views.searchPermission),

	path('create/', views.createPermission),

	path('update/<int:pk>', views.updatePermission),

	path('delete/<int:pk>', views.deletePermission),



]