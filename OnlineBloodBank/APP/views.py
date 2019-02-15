# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
# from  forms import UserForm,DonateModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.hashers import make_password
from models import DonarRegistation, BloodGroup
from django.contrib.auth.decorators import login_required

# Create your views here.
def Index(request):
	return render(request,'home.html')
def signup(request):
	# group=BloodGroup.objects.all()
	if request.method=="POST":
		# blood=BloodGroup.objects.get(id=request.POST.get("blood_id"))
		user=DonarRegistation.objects.create_user(cell_no=request.POST.get('cell_no'),
			             username=request.POST.get('username'),
			             password=request.POST.get('password'),
			             name=request.POST.get('name'),
			             addrees=request.POST.get('addrees'),
			             blood_group=request.POST.get('blood_group'))
		user.save()
		return redirect("/login_view/")


	return render(request,'DonarRegistation.html')
def login_view(request):
		request.session["user"] = None



		if request.method=="POST":
			user=authenticate(username=request.POST.get('username'),
			              password=request.POST.get('password'))
			msg=" login successfully"
			if user:
				user_profiles=DonarRegistation.objects.filter(user_ptr=user)
				print user_profiles
				if user_profiles:
					user_profile=user_profiles[0]
					print user_profile
					request.session['user']={"username":user.username,"id":user_profile.id}
					login(request, user)
				return redirect("/dashbord/")
			else:
				return render(request,'login.html',{"msg":"login failed"})
		return render(request,'login.html')
@login_required
def CreateBloodGroup(request):
	msg=" "

	if request.method=="POST":
		blood=BloodGroup(blood_group=request.POST.get("blood_group"))
		blood.save()
		msg="BloodGroup created success fully"
	return render(request,"CreateBloodGroup.html",{"msg":msg})
@login_required	
def donarlist(request):
	Group = request.GET.get("bloodGroup")
	if Group:
		blood = DonarRegistation.objects.filter(blood_group=Group)
	else:
		blood = DonarRegistation.objects.all()
	return render(request,"search.html",{"blood":blood})
@login_required	
def dashbord(request):
	
	return render(request,'base.html')
@login_required
def list(request):
	group=BloodGroup.objects.all()

	return render(request,'list.html',{"group":group})
@login_required
def updateprofile(request,pk):
	# bd=BloodGroup.object.all()
	user =DonarRegistation.objects.get(pk=pk)
	if request.method=="POST":
		# blood=BloodGroup.objects.get(id=request.POST.get("blood_id"))

		user_obj=DonarRegistation.objects.get(pk=pk)
		user_obj.cell_no=request.POST.get('cell_no')
		user_obj.name=request.POST.get('name')
		user_obj.addrees=request.POST.get('addrees')
		user_obj.blood_group=request.POST.get('blood_group')
		user_obj.save()
		return redirect("/dashbord/")

		# 		st_object.school_id=school_objP
		# st_object.section_id=scection_obj

	return render(request,"updateprofile.html",{"user":user})

def signout(request):
	if request.method=="POST":
		logout(request)
		return redirect(Index)
	return render(request,"logout.html")
