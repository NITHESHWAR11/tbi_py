from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#models
from .models import Latest_News_db, New_Events_db, Past_Events_db, Contact_SECTION

#utls import
from .Tools import reguler_datas

#-----------------------------------------------views--------------------------------------------------------------------------------------------

def Latest_news_delete(request):
    news_id = request.POST.get("id")
    delete_id = Latest_News_db.objects.get(id=news_id)
    delete_id.delete()
    return render(request, "pages/latest_News_edit.html", reguler_datas())

def Latest_news_save(request):
    Title = request.POST.get("#title")
    description = request.POST.get("#description")
    images = request.FILES["#fileInput-single_image"]
    obj = Latest_News_db(Title=Title, image_banner=images, description=description)
    obj.save()
    return render(request, "pages/latest_News_edit.html", reguler_datas())

@login_required(login_url='/FourNotFout')
def Latest_news_edit(request):
    try:
        Latest_News_formdata_db = Latest_News_db.objects.all()[::-1]
        return render(request, "pages/latest_News_edit.html", reguler_datas({'Latest_News_formdata_db':Latest_News_formdata_db}))
    except:
        print("Maybe No data in database")
    return render(request, "pages/latest_News_edit.html", reguler_datas())

#----------------------------------------------------------------------------------------------------------------------------

def New_event_delete(request):
    news_id = request.POST.get("id")
    delete_id = New_Events_db.objects.get(id=news_id)
    delete_id.delete()
    return render(request, "pages/new_events_edit.html", reguler_datas())

def New_event_save(request):
    Title = request.POST.get("#title")
    description = request.POST.get("#description")
    images = request.FILES["#fileInput-single_image"]
    obj = New_Events_db(Title=Title, image_banner=images, description=description)
    obj.save()
    return render(request, "pages/new_events_edit.html", reguler_datas())

@login_required(login_url='/FourNotFout')
def New_events_edit(request):
    try:
        New_Events_formdata_db = New_Events_db.objects.all()[::-1]
        return render(request, "pages/new_events_edit.html", reguler_datas({'New_Events_formdata_db':New_Events_formdata_db}))
    except:
        print("Maybe No data in database")
    return render(request, "pages/new_events_edit.html", reguler_datas())

#-------------------------------------------------------------------------------------------------------------------------------

def Past_event_delete(request):
    news_id = request.POST.get("id")
    delete_id = Past_Events_db.objects.get(id=news_id)
    delete_id.delete()
    return render(request, "pages/past_events_edit.html", reguler_datas())

def Past_event_save(request):
    Title = request.POST.get("#title")
    description = request.POST.get("#description")
    images = request.FILES["#fileInput-single_image"]
    obj = Past_Events_db(Title=Title, image_banner=images, description=description)
    obj.save()
    return render(request, "pages/past_events_edit.html", reguler_datas())

@login_required(login_url='/FourNotFout')
def Past_events_edit(request):
    try:
        Past_Events_formdata_db = Past_Events_db.objects.all()[::-1]
        return render(request, "pages/past_events_edit.html", reguler_datas({'Past_Events_formdata_db':Past_Events_formdata_db}))
    except:
        print("Maybe No data in database")
    return render(request, "pages/past_events_edit.html", reguler_datas())


#---------------------------------views for frentend---------------------------------------------------------------------------------

def New_events(request):
    try:
        New_Events_formdata_db = New_Events_db.objects.all()[::-1]
        contact_Section =  Contact_SECTION.objects.all()[::-1]
        return render(request, "new_events.html", reguler_datas({'New_Events_formdata_db':New_Events_formdata_db, 'cs':contact_Section}))
    except:
        print("Maybe No data in database")
    return render(request, "new_events.html", reguler_datas())

def Latest_events(request):
    try:
        Latest_News_formdata_db = Latest_News_db.objects.all()[::-1]
        contact_Section =  Contact_SECTION.objects.all()[::-1]
        return render(request, "latest_events.html", reguler_datas({'Latest_News_formdata_db':Latest_News_formdata_db, 'cs':contact_Section}))
    except:
        print("Maybe No data in database")
    return render(request, "latest_events.html", reguler_datas())

def past_events(request):
    try:
        Past_Events_formdata_db = Past_Events_db.objects.all()[::-1]
        contact_Section =  Contact_SECTION.objects.all()[::-1]
        return render(request, "past_events.html", reguler_datas({'Past_Events_formdata_db':Past_Events_formdata_db, 'cs':contact_Section}))
    except:
        print("Maybe No data in database")
    return render(request, "past_events.html", reguler_datas())
