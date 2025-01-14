from django.urls import path

from location.views import home_views as views


urlpatterns = [
	path('all/', views.home_view),


]