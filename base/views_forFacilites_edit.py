from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

#utls import
from .Tools import reguler_datas



@login_required(login_url='/FourNotFout')
def Iot_edit(request):
     return render(request,"pages/IOT_edit.html",reguler_datas())

@login_required(login_url='/FourNotFout')
def Healthcare_edit(request):
     return render(request,"pages/Healthcare_edit.html",reguler_datas())

@login_required(login_url='/FourNotFout')
def Design_and_development_edit(request):
     return render(request,"pages/Design_&_development_edit.html",reguler_datas())

@login_required(login_url='/FourNotFout')
def Support_service_edit(request):
     return render(request, "pages/Support_service_edit.html", reguler_datas())

@login_required(login_url='/FourNotFout')
def center_of_excellance_edit(request):
     return render(request, "pages/center_of_excellance_edit.html", reguler_datas())
