from django.urls import path
from app.views import home, admin, patient, receptioniste,provinces,communes,zones,public,specialites,users,cabinets,medecins,medecin,receptionistes,horaires, CreneauJournalier

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('home/',home.index, name = 'home'),
    
    #Admin
    path ('admin/home/',admin.index, name = 'admin_index'),
    
    path ('',users.user_login, name = 'user_login'),
    path ('logout/',users.user_logout, name = 'user_logout'),
    
    path ('admin/templates/provinces/',provinces.index, name = 'provinces_index'),
    path ('admin/templates/provinces/add',provinces.add, name = 'provinces_add'),
    path ('admin/templates/provinces/store',provinces.store, name = 'provinces_store'),
    path ('admin/templates/provinces/edit/<int:id>',provinces.edit, name = 'provinces_edit'),
    path ('admin/templates/provinces/update/<int:id>',provinces.update, name = 'provinces_update'),
    path ('admin/templates/provinces/delete/<int:id>',provinces.delete, name = 'provinces_delete'),



    path ('admin/templates/communes/',communes.index, name = 'communes_index'),
    path ('admin/templates/communes/add',communes.add, name = 'communes_add'),
    path ('admin/templates/communes/store',communes.store, name = 'communes_store'),
    path ('admin/templates/communes/edit/<int:id>',communes.edit, name = 'communes_edit'),
    path ('admin/templates/communes/update/<int:id>',communes.update, name = 'communes_update'),
    path ('admin/templates/communes/delete/<int:id>',communes.delete, name = 'communes_delete'),
    
    
    path ('admin/templates/zones/',zones.index, name = 'zones_index'),
    path ('admin/templates/zones/add',zones.add, name = 'zones_add'),
    path ('admin/templates/zones/store',zones.store, name = 'zones_store'),
    path ('admin/templates/zones/edit/<int:id>',zones.edit, name = 'zones_edit'),
    path ('admin/templates/zones/update/<int:id>',zones.update, name = 'zones_update'),
    path ('admin/templates/zones/delete/<int:id>',zones.delete, name = 'zones_delete'),
    path ('admin/templates/zones/getCommunes', zones.getCommunes, name = 'zones_getCommunes'),


    
    path ('admin/templates/specialites/',specialites.index, name = 'specialites_index'),
    path ('admin/templates/specialites/add',specialites.add, name = 'specialites_add'),
    path ('admin/templates/specialites/store',specialites.store, name = 'specialites_store'),
    path ('admin/templates/specialites/edit/<int:id>',specialites.edit, name = 'specialites_edit'),
    path ('admin/templates/specialites/update/<int:id>',specialites.update, name = 'specialites_update'),
    path ('admin/templates/specialites/delete/<int:id>',specialites.delete, name = 'specialites_delete'),


    
    path ('admin/templates/users/',users.index, name = 'users_index'),
    path ('admin/templates/users/add',users.add, name = 'users_add'),
    path ('admin/templates/users/store',users.store, name = 'users_store'),
    path ('admin/templates/users/edit/<int:id>',users.edit, name = 'users_edit'),
    path ('admin/templates/users/update/<int:id>',users.update, name = 'users_update'),
    path ('admin/templates/users/delete/<int:id>',users.delete, name = 'users_delete'),


   

    
    path ('admin/templates/medecins/',medecins.index, name = 'medecins_index'),
    path ('admin/templates/medecins/add',medecins.add, name = 'medecins_add'),
    path ('admin/templates/medecins/addredir',medecins.addredir, name = 'medecins_addredir'),
    path ('admin/templates/medecins/store',medecins.store, name = 'medecins_store'),
     path ('admin/templates/medecins/storeMed',medecins.storeMed, name = 'medecins_storeMed'),
    path ('admin/templates/medecins/edit/<int:id>',medecins.edit, name = 'medecins_edit'),
    path ('admin/templates/medecins/update/<int:id>',medecins.update, name = 'medecins_update'),
    path ('admin/templates/medecins/delete/<int:id>',medecins.delete, name = 'medecins_delete'),

#medecin
    path ('medecin/home/',medecin.index, name = 'medecin_index'),
    
    path ('medecin/templates/cabinets/',cabinets.index, name = 'cabinets_index'),
    path ('medecin/templates/cabinets/add',cabinets.add, name = 'cabinets_add'),
    path ('medecin/templates/cabinets/store',cabinets.store, name = 'cabinets_store'),
    path ('medecin/templates/cabinets/edit/<int:id>',cabinets.edit, name = 'cabinets_edit'),
    path ('medecin/templates/cabinets/update/<int:id>',cabinets.update, name = 'cabinets_update'),
    path ('medecin/templates/cabinets/delete/<int:id>',cabinets.delete, name = 'cabinets_delete'),
    path ('medecin/templates/cabinets/getCommunes', cabinets.getCommunes, name = 'cabinets_getCommunes'),
    path ('medecin/templates/cabinets/getZones', cabinets.getZones, name = 'cabinets_getZones'),
    
    
    path ('medecin/templates/receptionistes/',receptionistes.index, name = 'receptionistes_index'),
    path ('medecin/templates/receptionistes/user_add',receptionistes.addUser, name = 'receptionistes_addUser'),
    path ('medecin/templates/receptionistes/add',receptionistes.add, name = 'receptionistes_add'),
    path ('medecin/templates/receptionistes/store',receptionistes.store, name = 'receptionistes_store'),
    path ('medecin/templates/receptionistes/storeUser',receptionistes.storeUser, name = 'receptionistes_storeUser'),
    path ('medecin/templates/receptionistes/edit/<int:id>',receptionistes.edit, name = 'receptionistes_edit'),
    path ('medecin/templates/receptionistes/update/<int:id>',receptionistes.update, name = 'receptionistes_update'),
    path ('medecin/templates/receptionistes/delete/<int:id>',receptionistes.delete, name = 'receptionistes_delete'),

    
#patient
        path ('patient/home/',patient.index, name = 'patient_index'),
        
#receptioniste
    path ('receptioniste/home/',receptioniste.index, name = 'receptioniste_index'), 
         
    path ('receptioniste/templates/horaires/',horaires.index, name = 'horaires_index'),
    path ('receptioniste/templates/horaires/add',horaires.add, name = 'horaires_add'),
    path ('receptioniste/templates/horaires/store',horaires.store, name = 'horaires_store'),
    path ('receptioniste/templates/horaires/edit/<int:id>',horaires.edit, name = 'horaires_edit'),
    path ('receptioniste/templates/horaires/update/<int:id>',horaires.update, name = 'horaires_update'),
    path ('receptioniste/templates/horaires/delete/<int:id>',horaires.delete, name = 'horaires_delete'),
    
    path ('receptioniste/templates/creneauJournalier/',CreneauJournalier.index, name = 'creneauJournaliers_index'),
    path ('receptioniste/templates/creneauJournalier/add',CreneauJournalier.add, name = 'creneauJournaliers_add'),
    path ('receptioniste/templates/creneauJournalier/store',CreneauJournalier.store, name = 'creneauJournaliers_store'),
    path ('receptioniste/templates/creneauJournalier/edit/<int:id>',CreneauJournalier.edit, name = 'creneauJournaliers_edit'),
    path ('receptioniste/templates/creneauJournalier/update/<int:id>',CreneauJournalier.update, name = 'creneauJournaliers_update'),
    path ('receptioniste/templates/creneauJournalier/delete/<int:id>',CreneauJournalier.delete, name = 'creneauJournaliers_delete'),
    
    
    #public
    path ('public/home/',public.index, name = 'public_index'),
    path ('public/templates/med_descriptions/<int:id>',public.description, name = 'public_med_description'),
    path ('public/templates/choix_creneau/<int:id>',public.choix_créneaux, name = 'public_med_choix_créneaux'),
       
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



  