from django.contrib import admin
from base import views, views_forFacilites_edit, views_for_facilites, views_for_newsandevents
from django.urls import path
from Crescent import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    
    path('admin_home', admin.site.urls),
    path('', views.home),
    path('image_upload_page_gallery',views.image_upload_page_gallery),

    path('admin',views.admin_home),
    path('admin_home_auth',views.admin_home_auth),
    path('logout_admin',views.logout_admin),
    path('FourNotFout',views.FourNotFout),

    path('upload_image',views.upload_image),
    path('delete_image',views.delete_image),
    
    path('team',views.aboutus),
    path('admin_team',views.admin_team),
    path('update_team',views.update_team),
    path('delete_team',views.delete_team),

    path('birac',views.birac),
    path('birac_edit',views.birac_edit),
    path('birac_save',views.birac_save),
    path('delete_birac',views.delete_birac),
    path('set_birac',views.set_birac),
    path('facilities_developed_save',views.facilities_developed_save),
    path('delete_facilities_developed',views.delete_facilities_developed),



    path('logo',views.update_logo),
    path('upload_logo',views.upload_logo),
    path('delete_logo',views.delete_logo),
    path('set_logo',views.set_logo),

    path('carrer',views.carrer),
    path('update_carrer',views.update_carrer),
    path('edit_eventform',views.edit_eventform),


    path('eventform',views.eventform),
    path('update_eventform',views.update_eventform),
    path('delete_form',views.delete_form),


    path('download_pdf',views.download_pdf),      # Download home pdf
    path('convert_excel',views.convert_excel),
    path('carrer_convert_excel',views.carrer_convert_excel), # >>>>>>>>>>>>>>>>>>>>>>>> Download Files >>>>>>>>>>>>>>>>>>>>
    
    
    path('list_blog',views.list_blog),
    path('list_edit_blog',views.list_edit_blog),
    path('view_blog/<str:pk>',views.view_blog),
    path('edit_blog/<str:pk>',views.edit_blog),
    path('blog_edit',views.blog_edit),
    path('save_blog',views.save_blog),
    path('delete_blog',views.delete_blog),
    path('edit_blog/save_edit_blog/<int:pk>',views.save_edit_blog),

    path('testimonicals',views.Testimonicals),
    path('testimonicals_edit',views.Testimonicals_edit),
    path('testimonicals_save',views.Testimonicals_save),
    path('delete_Testimonicals',views.delete_Testimonicals),

    path('events',views.events),
    path('events_save',views.events_save),
    path('events_edit',views.events_edit),

    path('tbi',views.tbi),
    path('tbi_edit',views.tbi_edit),
    path('tbi_save',views.tbi_save),
    path('delete_tbi',views.delete_tbi),
    path('set_tbi',views.set_tbi),

    path('sisfs',views.sisfs),
    path('sisfs_edit',views.sisfs_edit),
    path('sisfs_save',views.sisfs_save),
    path('delete_sisfs',views.delete_sisfs),
    path('set_sisfs',views.set_sisfs),
    path('SISFS_scheme_save',views.SISFS_scheme_save),
    path('delete_SISFS_scheme',views.delete_SISFS_scheme),


    # path("about",views.about),
    path("about_edit",views.about_edit),
    
   
    path("Home",views.home),
    
    path("Mentor_Connect",views.MentorConnect),
    path("Mentor_Connect_edit",views.MontorConnect_edit),
    path("Mentor_Connect_save",views.MontorConnect_save),

    path("MBA",views.MBA),
    path("MBA_edit",views.MBA_edit),
    path("MBA_save",views.MBA_save),

    path("Mentor_Clinic",views.MentorClinic),
    path("Mentor_Clinic_edit",views.Mentor_Clinic_edit),
    path("Mentor_Clinic_save",views.Mentor_Clinic_save),

    path("angelInvestor",views.angelInvestor),
    path("angelInvestor_edit",views.angelInvestor_edit),
    path("angelInvestor_save",views.angelInvestor_save),

    path("new_ventures",views.new_ventures),
    path("new_ventures_edit",views.new_ventures_edit),
    path("new_ventures_save",views.new_ventures_save),

    path("CentralGovernmentFunding",views.CentralGovernmentFunding),
    path("CentralGovernmentFunding_edit",views.CentralGovernmentFunding_edit),
    path("CentralGovernmentFunding_save",views.CentralGovernmentFunding_save),

    path("ourstartups",views.ourStartups),
    path("ourStartups_edit",views.ourStartups_edit),
    path("ourStartups_save",views.ourStartups_save),
    path("ourStartups_logo_save", views.ourStartups_logo_save),
    path("delete_startup",views.delete_startup),
    path("delete_ourStartups_logo_save", views.delete_ourStartups_logo_save),

    path('pre_incubation', views.ourstartup_pre_Incubation),
    path("incubation", views.ourstartup_Incubation),
    
    path("sisfs",views.sisfs),
    path("testimonial",views.testimonial),
     
    path("career",views.career),
    path("gallery",views.gallery),

    path("home_edit",views.home_edit),
    path("whoweare_save",views.Whoweare),
    path("HomePdfLink_save",views.HomePdfLink_save),
    path("Home_TESTIMONIAL",views.Home_TESTIMONIAL),
    path("Contact_Section",views.Contact_Section),
    path("investors",views.investors),
    path("International_Partners",views.International),
    path("Govt_Tie",views.GovtTie),
    path("upload_images",views.Upload_Image),
    path("delete_upload",views.delete_upload),
    path("delete_investors",views.delete_investors),
    path("delete_Govt_Tie",views.delete_Govt_Tie),
    path("delete_Internationalpartners",views.delete_Internationalpartners),

    path("HowWeWork_save",views.HowWeWork_save),
    path("Last_content_save",views.Last_content_save),
    path("About_heading_save",views.About_heading_save),

    path("mentor", views.Mentor_page),
    path("Mentors_page_edit", views.Mentors_page_edit),
    path('Mentors_page_save', views.Mentors_page_save),
    path('Mentor_page_delete', views.Mentor_page_delete),
    path('nonTechinal_mentor', views.nontechnical_page),
    path('technical', views.technical_page),
    
    path("teams", views.Teams_page),
    path("Teams_page_edit", views.Teams_page_edit),
    path('Teams_page_save', views.Teams_page_save),
    path('Team_page_delete', views.Teams_page_delete),

    path("service",views.service),
    path("service_edit",views.service_edit),
    path("TopSection_save",views.TopSection_save),
    path("WhatWedo_save",views.WhatWedo_save),
    path("Our_Process_save",views.Our_Process_save),
    path("Spending_Section_save",views.Spending_Section_save),
    path("Join_Our_Community_save",views.Join_Our_Community_save),



    path("globalMarket",views.Global_Market),
    path("GlobalMarket_edit",views.GlobalMarket_edit),
    path("GlobalMarket_save",views.GlobalMarket_save),
    path("GlobalMarketPic_save",views.GlobalMarketPic_save),
    path("set_GlobalMarketPic",views.set_GlobalMarketPic),
    path("delete_GlobalMarketPic",views.delete_GlobalMarketPic),

    path("demoday",views.demoday),
    path("demoday_edit",views.demoday_edit),
    path("DemoDayTOPSECTION_save",views.DemoDayTOPSECTION_save),
    path("DemoDayPic_save",views.DemoDayPic_save),
    path("set_DemoDayPic",views.set_DemoDayPic),
    path("delete_DemoDayPic",views.delete_DemoDayPic),

    path("stategovtfunds",views.stategovtfunds),
    path("stategovtfunds_edit",views.stategovtfunds_edit),
    path("StateGovtFund_save",views.StateGovtFund_save),
    path("StateGovtFundSecondSection_save",views.StateGovtFundSecondSection_save),
    path("StateGovtFundEligibilitySection_save",views.StateGovtFundEligibilitySection_save),

    path("startuptn",views.startuptn),
    path("startuptn_edit",views.startuptn_edit),
    path("Start_UpTN_save",views.Start_UpTN_save),
    path("Start_UpTNContent2_save",views.Start_UpTNContent2_save),
    path("Start_UpTNimg1_save",views.Start_UpTNimg1_save),
    path("Start_UpTNimg2_save",views.Start_UpTNimg2_save),
 
    path("samridth",views.samridth),
    path("samridth_edit",views.samridth_edit),
    path("SamridthFund_save",views.SamridthFund_save),
    path("MeitY_SAMRIDH_save",views.MeitY_SAMRIDH_save),
    path("BundledServices_save",views.BundledServices_save),

    path("edi",views.edi),
    path("edi_edit",views.edi_edit),
    path("EDI_TOPSECTION_save",views.EDI_TOPSECTION_save),
    path("EDI_Overview_Section_save",views.EDI_Overview_Section_save),
    path("EDI_InnovationVoucher_save",views.EDI_InnovationVoucher_save),
    path("EDI_WeAimAtSection_save",views.EDI_WeAimAtSection_save),
    path("EDI_Eligibility_Section_save",views.EDI_Eligibility_Section_save),

    path('fishieriespage',views.fishieriespage),
    path('ivp',views.ivppage),
    path('asiim',views.asiimpage),
    path('fishieries',views.update_fishieries),
    path('upload_fishieries',views.upload_fishieries),
    path('delete_fishieries',views.delete_fishieries),
    path('set_fishieries',views.set_fishieries),

    path('contact_edit',views.contact_edit),
    path('ContactEditPage_save',views.ContactEditPage_save),
    path('contact',views.contact),

    path("thiruabout", views.about),

    path('footer_edit',views.footer_edit),
    path('FooterEditPage_save',views.FooterEditPage_save),
    path('SocialMediaLinks_save',views.SocialMediaLinks_save),
    
    path('category',views.category),
    path('CategoryforGallery_save',views.CategoryforGallery_save),
    path('delete_CategoryforGallery',views.delete_CategoryforGallery),

    path('delete_CategoryforGallery',views.delete_CategoryforGallery),


    path('CategoryforTeams',views.CategoryforTeams),
    path('CategoryforTeams_save',views.CategoryforTeams_save),
    path('delete_CategoryforTeams',views.delete_CategoryforTeams),
    
    path('CategoryforEvents_save',views.CategoryforEvents_save),
    path('delete_CategoryforEvents',views.delete_CategoryforEvents),

    path('CategoryforQualification_save',views.CategoryforQualification_save),
    path('delete_CategoryforQualification',views.delete_CategoryforQualification),

    path('CategoryforExperience_save',views.CategoryforExperience_save),
    path('delete_CategoryforExperience',views.delete_CategoryforExperience),

    path('CategoryforBlogs_save',views.CategoryforBlogs_save),
    path('delete_CategoryforBlogs',views.delete_CategoryforBlogs),

    path('CategoryforStartups_save',views.CategoryforStartups_save),
    path('scrolling_text_save', views_forFacilites_edit.scrolling_text_save),
#--facility--
    path("IOT_edit", views_forFacilites_edit.Iot_edit),
    path("healthcare_edit", views_forFacilites_edit.Healthcare_edit),
    path("designanddevelopment_edit", views_forFacilites_edit.Design_and_development_edit),
    path("support_service_edit", views_forFacilites_edit.Support_service_edit),
    path("center_of_excellance",views_forFacilites_edit.center_of_excellance_edit),

#--facellity_save------
    path("Iot_edit_save", views_forFacilites_edit.Iot_edit_save),
    path("health_care_edit_save", views_forFacilites_edit.helthcare_edit_save),
    path("design_and_developmeth_save", views_forFacilites_edit.design_and_development_edit_save),
    path("center_of_eormate_save", views_forFacilites_edit.center_of_excellance_edit_save),
    path("support_service_edit_save", views_forFacilites_edit.Support_service_edit_save),

#--facellity_save----
    path("Iot_delete", views_forFacilites_edit.Iot_delete),
    path("healthcare_delete", views_forFacilites_edit.helthcare_delete),
    path("support_and_development_delete", views_forFacilites_edit.Support_development_delete),
    path("center_of_excelence_delete", views_forFacilites_edit.Center_of_excellance_delete),

    #-----------------------------------facielty frontend-------------------------------------------------------------------------
    path("Iot", views_for_facilites.Iot),
    path("healthcare", views_for_facilites.Healthcare),
    path("design_development", views_for_facilites.Design_and_Developmentfre),
    path("support_and_service", views_for_facilites.Support_servisefre),
    path("center_of_excellancefre", views_for_facilites.Center_of_excellancefre),

    #----------------------------------News and Events edit ----------------------------------------------------------------------
    path("latest_news_edit", views_for_newsandevents.Latest_news_edit),
    path("new_events_edit", views_for_newsandevents.New_events_edit),
    path("past_events_edit", views_for_newsandevents.Past_events_edit),
    #---------------------------------News and Events save------------------------------------------------------------------------
    path("latest_news_save", views_for_newsandevents.Latest_news_save),
    path("New_event_save", views_for_newsandevents.New_event_save),
    path("Past_event_save", views_for_newsandevents.Past_event_save),
    #--------------------------------News and Evemts delete------------------------------------------------------------------------
    path("Latest_news_delete", views_for_newsandevents.Latest_news_delete),
    path("New_event_delete", views_for_newsandevents.New_event_delete),
    path("Past_event_delete", views_for_newsandevents.Past_event_delete),
    #-------------------------------->news and events frentand---------------------------------------------------------------------
    path("Latest_events",views_for_newsandevents.Latest_events),
    path("New_events", views_for_newsandevents.New_events),
    path("past_events", views_for_newsandevents.past_events),
    path("about", views.about_us),
    
    #------------------------------------------->Home Screen Banner<--------------------------------------------------------------
    path("home_screen_banner_save", views.home_screen_banner_save),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + staticfiles_urlpatterns()


#quver, versal
