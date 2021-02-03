from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import datetime
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


# Create your views here.

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_authentication_status(request, *args, **kwargs):
	"""This API returns a text if the user is authenticated."""

	return Response(data="You were successfully able to use the API", status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def change_email(request, *args, **kwargs):
	"""Change User email after validating the password entered."""

	if check_password(request.data['current_password'], request.user.password):
		if request.data['new_email'] == request.data['re_new_email']:
			user_obj = User.objects.get(id=request.user.id)
			user_obj.email = request.data['new_email']
			user_obj.save()
			return Response(data="User email has been successfully updated!", status=status.HTTP_200_OK)
		else:
			return Response(data="The email inputs do not match!", status=status.HTTP_400_BAD_REQUEST)
	return Response(data="Password incorrect!", status=status.HTTP_400_BAD_REQUEST)