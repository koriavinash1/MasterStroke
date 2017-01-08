from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse,Http404
import models
import json

def userlogin(request):
    return render(request,'index.html',{})
