from django.conf.urls.defaults import *
import settings 
from settings import MEDIA_ROOT, DEBUG
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'afrikimage.views.home',name='home'),

    url(r'^auteur$', 'afrikimage.views.auteur',name='auteur'),

    url(r'^galerie(?P<num>\d+)*$','afrikimage.views.galerie',name='galerie'),

    url(r'^photographes-(?P<num>\d+)*$', 'afrikimage.views.photographe',name='photographe'),

    url(r'^ajoutphoto-(?P<num>\d+)*-(?P<id>\d+)*-(?P<actid>\d+)*-(?P<objid>\d+)*-(?P<habid>\d+)*-(?P<img>\d+)*$' , 'afrikimage.views.add_photo',name='ajoutphoto'),

    url(r'^delete_confirm_photo-(?P<num>\d+)*$' , 'afrikimage.views.delete_confirm_photo' , name = 'delete_confirm_photo'),

    url(r'^deleting_photo-(?P<num>\d+)*$' , 'afrikimage.views.deleting_photo' , name ='deleting_photo'),

    url(r'^image(?P<num>\d+)*-(?P<id>\d+)*-(?P<actid>\d+)*-(?P<objid>\d+)*-(?P<habid>\d+)*$' , 'afrikimage.views.add_image' ,name ='image' ),
    
    url(r'^modif_image-(?P<id>\d+)-(?P<num>\d+)*$' , 'afrikimage.views.modif_image' , name = 'modif_image'),
    
    url(r'^delete_confirm_auteur-(?P<num>\d+)*$' , 'afrikimage.views.delete_confirm_auteur' , name = 'delete_confirm_auteur'),

    url(r'^deleting_auteur-(?P<num>\d+)*$' , 'afrikimage.views.deleting_auteur' , name = 'deleting_auteur' ),

    url(r'^ajoutautor$', 'afrikimage.views.add_autor',name='ajoutautor'),

    url(r'^infoauteur-(?P<id>\d+)$','afrikimage.views.infoauteur',name='infoauteur'),

    url(r'^ajout_lieux$' , 'afrikimage.views.add_lieux' , name = 'ajout_lieux'),

    url(r'^modif_auteur-(?P<id>\d+)$','afrikimage.views.modif_auteur' , name = 'modif_auteur'),

    url(r'^info_photo-(?P<num>\d+)*$', 'afrikimage.views.info_photo', name = 'info_photo'),

    url(r'^dashphoto-(?P<num>\d+)$' , 'afrikimage.views.dashphoto' , name = 'dashphoto'),

    url(r'^modif_photo-(?P<id>\d+)-((?P<num>\d+)*)*$' , 'afrikimage.views.modif_photo' , name = 'modif_photo'),

    url(r'^ajout_personne-(?P<id>\d+)*$','afrikimage.views.add_personne', name = 'ajout_personne'),

    url(r'^ajout_action-(?P<lied>\d+)*-(?P<persid>\d+)*$' , 'afrikimage.views.add_action' , name = 'ajout_action'),

    url(r'^ajout_objet-(?P<lied>\d+)*-(?P<persid>\d+)*-(?P<actid>\d+)*$' , 'afrikimage.views.add_objet' , name = 'ajout_objet'),

    url(r'^ajout_habit-(?P<lied>\d+)*-(?P<persid>\d+)*-(?P<actid>\d+)*-(?P<objid>\d+)*$' , 'afrikimage.views.add_habillement' , name = 'ajout_habit'),
    
    
    
    
    url(r'^admin/', include('smuggler.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^static/(?P<path>.*)$', 
             'django.views.static.serve',
             {'document_root': MEDIA_ROOT, 'show_indexes': True}),

)
handler404 = "galerie.afrikimage.views.my_custom_404_view"
