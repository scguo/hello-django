# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.conf import settings

def landing(request):
	return render(request, 'base.html')