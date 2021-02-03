from django.urls import path, include
from account_processes import views

urlpatterns = [
	path("", include('djoser.urls')),
	path("", include('djoser.urls.authtoken')),
	path("authentication_status/", views.get_authentication_status),
	path("set_email/", views.change_email)
]