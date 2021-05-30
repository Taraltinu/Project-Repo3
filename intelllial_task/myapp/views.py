from django.shortcuts import render,HttpResponse,redirect
import requests
# Create your views here.
from django.views import View
from django.http import JsonResponse


# i'm also try with token base but its not working like this

'''def get_token():
	URL = "https://reqres.in/api/login" 
	response = requests.post(URL,data={"email":email,"password":password})
	if response.status_code ==200:
		return response.json()
	else:
		return response.json()

def fetch_users(page):
	page = page
	url = f"https://reqres.in/api/users?page={id}"
	header = {"Authorization":f'Token{get_token()}'}
	response = requests.get(URL,headers=header)
	if response.status_code==200:
		return JsonResponse(response.json(),safe=True)
	else:
		return JsonResponse(response.json(),safe=True)'''
#but its not working 





class Login(View):
	template_name = 'login.html'
	def get(self,request):
		return render(request, self.template_name)
	def post(self,request):
		email = request.POST.get("email")#"eve.holt@reqres.in"
		password = request.POST.get("password")#"cityslicka"

		URL = "https://reqres.in/api/login" 
		response = requests.post(URL,data={"email":email,"password":password})
		if response.status_code ==200:
			return redirect("user_list")
		else:
			return redirect('/')
		return render(request, self.template_name)



#login view start
class User_Get(View):
	def get(self,request):
		id= request.GET.get('page', None)
		URL = f"https://reqres.in/api/users?page={id}"
		res = requests.get(url = URL).json()
		return JsonResponse(res)



#login view end




#user list view view start
class UserList(View):
	template_name = "user_list.html"
	def get(self,request):
		id= request.GET.get('page', None)
		URL = f"https://reqres.in/api/users?page={id}"
		res = requests.get(url = URL).json()
		return render(request, self.template_name,{"user_list":res})



#user list view end

