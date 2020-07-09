from .views import *

# get_all=GetView()
# add_view=CreateView()
create_user=CreateUser()
get_users=UserList()
get_user=UserDetail()
# def list_fun(request):
# 	if request.method=='GET':
# 		data=get_all.get(request)
# 		print(data.context_data)
# 		list_data=data.data
# 		return render(request,'base.html',{"list_data":list_data})


# def post_view(request):
# 	return render(request,'create.html')


# def addview(request):
# 	if request.method=="POST":
# 		data=add_view.post(request)
# 		list_data=data.data
# 		print(list_data)
# 	return render(request,'create.html')

from django.shortcuts import render,redirect
# from  forms import UserForm,DonateModelForm

def reg_view(request):
 	return render(request,"reg.html")

def addreg(request):
	if request.method=="POST":
		print("addreg")
		data=create_user.post(request)
		list_data=data.data
		print(list_data)
		if list_data:
			return redirect("/login_view/")
		else:
			return render(request,'reg.html')
def All_User(request):
	if request.method=='GET':
		data=get_users.get(request)
		print(data.context_data)
		list_data=data.data
		return render(request,'base.html',{"list_data":list_data})


def user_detailes(request,pk):
	if request.method=='GET':
		data=get_user.get(request,pk)
		print(data.context_data)
		list_data=data.data
		return render(request,'user.html',{"list_data":list_data})

