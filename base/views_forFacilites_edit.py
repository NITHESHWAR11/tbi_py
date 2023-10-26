from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

#models
from .models import Iot_form, HealthCare_form, Design_And_Development, Support_servise, Center_of_excellance, Home_Scrolling_text

#utls import
from .Tools import reguler_datas


def Iot_edit_save(request):
     Title = request.POST.get("#title")
     contant = request.POST.get("#content")
     Key_Points_1 = request.POST.get("#Key_Points_1")
     Key_Points_2 = request.POST.get("#Key_Points_2")
     Key_Points_3 = request.POST.get("#Key_Points_3")
     images = request.FILES["#fileInput-single_image"]
     obj = Iot_form(title_iot=Title, contant_iot=contant, image_iot=images, key_point1=Key_Points_1, key_point2=Key_Points_2, key_point3=Key_Points_3)
     obj.save()
     return render(request, "pages/IOT_edit.html", reguler_datas())

def Iot_delete(request):
    bl_id = request.POST.get("id")
    logo = Iot_form.objects.get(id=bl_id)
    logo.delete()
    return render(request, "pages/IOT_edit.html", reguler_datas())

@login_required(login_url='/FourNotFout')
def Iot_edit(request):
     try:
          Iot_form_db = Iot_form.objects.all()[::-1]
          return render(request,"pages/IOT_edit.html",reguler_datas({"Iot_form_db": Iot_form_db}))
     except:
          print("maybe database are empty")
     return render(request,"pages/IOT_edit.html",reguler_datas())

def helthcare_edit_save(request):
     Title = request.POST.get("#title")
     contant = request.POST.get("#content")
     Key_Points_1 = request.POST.get("#Key_Points_1")
     Key_Points_2 = request.POST.get("#Key_Points_2")
     Key_Points_3 = request.POST.get("#Key_Points_3")
     images = request.FILES["#fileInput-single_image"]
     obj = HealthCare_form(title_iot=Title, contant_iot=contant, image_iot=images, key_point1=Key_Points_1, key_point2=Key_Points_2, key_point3=Key_Points_3)
     obj.save()
     return render(request,"pages/Healthcare_edit.html",reguler_datas())

def helthcare_delete(request):
    bl_id = request.POST.get("id")
    logo = HealthCare_form.objects.get(id=bl_id)
    logo.delete()
    return render(request, "pages/IOT_edit.html", reguler_datas())

@login_required(login_url='/FourNotFout')
def Healthcare_edit(request):
     try:
          Healthcare_form_db = HealthCare_form.objects.all()[::-1]
          return render(request,"pages/Healthcare_edit.html",reguler_datas({"Healthcare_form_db": Healthcare_form_db}))
     except:
          print("maybe database are empty")
     return render(request,"pages/Healthcare_edit.html",reguler_datas())

def design_and_development_edit_save(request):
     Title = request.POST.get("#title")
     contant = request.POST.get("#content")
     Key_Points_1 = request.POST.get("#Key_Points_1")
     Key_Points_2 = request.POST.get("#Key_Points_2")
     Key_Points_3 = request.POST.get("#Key_Points_3")
     images = request.FILES["#fileInput-single_image"]
     obj = Design_And_Development(title_iot=Title, contant_iot=contant, image_iot=images, key_point1=Key_Points_1, key_point2=Key_Points_2, key_point3=Key_Points_3)
     obj.save()
     return render(request,"pages/Design_&_development_edit.html",reguler_datas())

def design_devlopment_delete(request):
    bl_id = request.POST.get("id")
    logo = Design_And_Development.objects.get(id=bl_id)
    logo.delete()
    return render(request, "pages/Design_&_development_edit.html", reguler_datas())

@login_required(login_url='/FourNotFout')
def Design_and_development_edit(request):
     try:
          Design_And_Development_db = Design_And_Development.objects.all()[::-1]
          return render(request,"pages/Design_&_development_edit.html",reguler_datas({"Design_And_Development_db":Design_And_Development_db}))
     except:
          print("maybe database are empty")
     return render(request,"pages/Design_&_development_edit.html",reguler_datas())


def Support_service_edit_save(request):
     Title = request.POST.get("#title")
     contant = request.POST.get("#content")
     Key_Points_1 = request.POST.get("#Key_Points_1")
     Key_Points_2 = request.POST.get("#Key_Points_2")
     Key_Points_3 = request.POST.get("#Key_Points_3")
     images = request.FILES["#fileInput-single_image"]
     obj = Support_servise(title_iot=Title, contant_iot=contant, image_iot=images, key_point1=Key_Points_1, key_point2=Key_Points_2, key_point3=Key_Points_3)
     obj.save()
     return render(request, "pages/Support_service_edit.html", reguler_datas())

def Support_development_delete(request):
    bl_id = request.POST.get("id")
    logo = Support_servise.objects.get(id=bl_id)
    logo.delete()
    return render(request, "pages/Support_service_edit.html", reguler_datas())

@login_required(login_url='/FourNotFout')
def Support_service_edit(request):
     try:
          support_development_db = Support_servise.objects.all()[::-1]
          return render(request, "pages/Support_service_edit.html", reguler_datas({"support_development_db":support_development_db}))
     except:
          print("maybe database are empty")
     return render(request, "pages/Support_service_edit.html", reguler_datas())

def center_of_excellance_edit_save(request):
     Title = request.POST.get("#title")
     contant = request.POST.get("#content")
     Key_Points_1 = request.POST.get("#Key_Points_1")
     Key_Points_2 = request.POST.get("#Key_Points_2")
     Key_Points_3 = request.POST.get("#Key_Points_3")
     images = request.FILES["#fileInput-single_image"]
     obj = Center_of_excellance(title_iot=Title, contant_iot=contant, image_iot=images, key_point1=Key_Points_1, key_point2=Key_Points_2, key_point3=Key_Points_3)
     obj.save()
     return render(request, "pages/center_of_excellance_edit.html", reguler_datas())

def Center_of_excellance_delete(request):
    bl_id = request.POST.get("id")
    logo = Center_of_excellance.objects.get(id=bl_id)
    logo.delete()
    return render(request, "pages/Support_service_edit.html", reguler_datas())

@login_required(login_url='/FourNotFout')
def center_of_excellance_edit(request):
     try:
          center_of_excellance_db = Center_of_excellance.objects.all()[::-1]
          return render(request, "pages/center_of_excellance_edit.html", reguler_datas({"center_of_excellance_db":center_of_excellance_db}))
     except:
          print("maybe database are empty")
     return render(request, "pages/center_of_excellance_edit.html", reguler_datas())
     

def scrolling_text_save(request):
     scrolling_text = request.POST.get("#scrolling_text")
     obj = Home_Scrolling_text(scrolling_text=scrolling_text)
     obj.save()
     return render(request,"pages/home_edit.html",reguler_datas())
