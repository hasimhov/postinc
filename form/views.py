# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import User
# Create your views here.

def formopen(request):
	return render(request,'form.html',{})
def formdata(request):
	name = request.POST['name']
	username = request.POST['bdate']
	desig = request.POST['pwd']
	locations = request.POST['email']
	skills = request.POST['phoneno']
	edu = request.POST['edu']
	about = request.POST['about']
	image = request.FILES['image']
	u = User(name=name,username=username,desig=desig,skills=skills,edu=edu,about=about,locations=locations,image=image)
	u.save()
	return redirect('/form/')
def formcomplete(request):
	return render(request,'compl.html',{})

