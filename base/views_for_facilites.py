from django.shortcuts import render

#models
from .models import Iot_form, HealthCare_form, Design_And_Development, Support_servise, Center_of_excellance, Contact_SECTION

#utls import
from .Tools import reguler_datas


def Iot(request):
    try:
        iot_formdata = Iot_form.objects.all()[::-1]
        contact_Section =  Contact_SECTION.objects.all()[::-1]
        return render(request, "iot.html", reguler_datas({'Iot_form':iot_formdata, 'cs':contact_Section}))
    except:
        print("Maybe No data in database")
    return render(request, "iot.html", reguler_datas())

def Healthcare(request):
    try:
        healthcare_formdata = HealthCare_form.objects.all()[::-1]
        contact_Section =  Contact_SECTION.objects.all()[::-1]
        return render(request, "Healthcare.html", reguler_datas({'healthcare_formdata':healthcare_formdata, 'cs':contact_Section}))
    except:
        print("Maybe No data in database")
    return render(request, "Healthcare.html", reguler_datas())

def Design_and_Developmentfre(request):
    try:
        design_development_formdata_db = Design_And_Development.objects.all()[::-1]
        contact_Section =  Contact_SECTION.objects.all()[::-1]
        return render(request, "Design_and_Development.html", reguler_datas({'design_development_formdata_db':design_development_formdata_db, 'cs':contact_Section}))
    except:
        print("Maybe No data in database")
    return render(request, "Design_and_Development.html", reguler_datas())
    
def Support_servisefre(request):
    try:
        Support_servise_formdata_db = Support_servise.objects.all()[::-1]
        contact_Section =  Contact_SECTION.objects.all()[::-1]
        return render(request, "Support_servise.html", reguler_datas({'Support_servise_formdata_db':Support_servise_formdata_db, 'cs':contact_Section}))
    except:
        print("Maybe No data in database")
    return render(request, "Support_servise.html", reguler_datas())

def Center_of_excellancefre(request):
    try:
        Center_of_excellance_formdata_db = Center_of_excellance.objects.all()[::-1]
        contact_Section =  Contact_SECTION.objects.all()[::-1]
        return render(request, "Center_of_excellance.html", reguler_datas({'Center_of_excellance_formdata_db':Center_of_excellance_formdata_db, 'cs': contact_Section}))
    except:
        print("Maybe No data in database")
    return render(request, "Center_of_excellance.html", reguler_datas())
