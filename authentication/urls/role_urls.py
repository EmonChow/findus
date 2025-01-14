
from django.urls import path
from authentication.views import role_views as views


urlpatterns = [
	path('all/', views.getAllRole),

	path('without_pagination/all/', views.getAllRoleWithoutPagination),

	path('<int:pk>', views.getARole),

	path('search/', views.searchRole),

	path('create/', views.createRole),

	path('update/<int:pk>', views.updateRole),

	path('delete/<int:pk>', views.deleteRole),

]