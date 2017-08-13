# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import User
# Create your views here.

def formopen(request):
	return render(request,'form.html',{})
def formdata(request):
	name = request.POST['name']
	username = request.POST['uname']
	desig = request.POST['desig']
	locations = request.POST['loc']
	skills = request.POST['skills']
	edu = request.POST['edu']
	about = request.POST['about']
	image = request.FILES['image']
	u = User(name=name,username=username,desig=desig,skills=skills,edu=edu,about=about,locations=locations,image=image)
	u.save()
	return redirect('/form/compl')
def formcomplete(request):
	return render(request,'compl.html',{})

