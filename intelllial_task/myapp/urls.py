from django.urls import re_path,path

from .views import *



urlpatterns = [

	path("",User_Get.as_view(),name="get_data"),
	path("user_list/",UserList.as_view(),name='user_list'),
	# path("page-data")
	path("login/",Login.as_view(),name="login"),


]