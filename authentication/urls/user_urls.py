from authentication.views import user_views as views
from django.urls import path

urlpatterns = [
	path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
	
]
