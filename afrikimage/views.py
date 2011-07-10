from django.shortcuts import render_to_response,HttpResponseRedirect
from afrikimage.models import * 
from form import ( SearchForm , PhotoForm , Autorform , LieuxForm , 
                   PersonneForm , Modif_Autorform , modif_photoform ,
                   ActionForm , ObjetForm , HabillementForm , ImageForm)
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from django.http import Http404
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms.formsets import formset_factory
from django.db.models import Q



def my_custom_404_view(request):
    """
    """
    return render_to_response('404.html', {})

def home(request):
    a = Photo.objects.order_by("-date")[:5]
    
    return render_to_response('home.html',{'a':a})

def photographe (request,*args, **kwargs):
    num = kwargs["num"] or 1
    photogr = Auteur.objects.all()
    paginator = Paginator(photogr,25)
    try:
        page = paginator.page(int(num))
    except EmptyPage:
        raise Http404
    #s'execute si le numero de la page est 2
    page.is_before_first = (page.number == 2)
    #si le numero de la page est egale au numero de l'avant 
    #de l'anvant dernier
    page.is_before_last = (page.number == paginator.num_pages - 1)
    #on constitue l'url de la page suivante
    page.url_next = reverse('photographe', args=[int(num) + 1])
    #on constititue l'url de page precedente
    page.url_previous = reverse('photographe',args=[int(num) - 1])
    #constitue l'url de la premiere page
    page.url_first = reverse('photographe')
    #on constitue l'url de la derniere page
    page.url_last = reverse('photographe', args = [paginator.num_pages])
    ctx = {'page':page,'paginator':paginator,'photogr':photogr}
    return render_to_response('photographe.html', ctx)

def infoauteur(request,*args, **kwargs):
    id_ = kwargs["id"]
    autor = Auteur.objects.filter(id = id_)
    
    context = {'autor':autor}
    return render_to_response('infoauteur.html',context)

def galerie(request,*args, **kwargs):
    num = kwargs["num"] or 1
    photo = Photo.objects.select_related().order_by("photographe__nom")
    paginator = Paginator(photo,20)
    try:
        page = paginator.page(int(num))
        
    except EmptyPage:

        raise Http404
    #s'execute si le numero de la page est 2
    page.is_before_first = (page.number == 2)
    #si le numero de la page est egale au numero de l'avant 
    #de l'anvant dernier
    page.is_before_last = (page.number == paginator.num_pages - 1)
    #on constitue l'url de la page suivante
    page.url_next = reverse('galerie', args=[int(num) + 1])
    #on constititue l'url de page precedente
    page.url_previous = reverse('galerie',args=[int(num) - 1])
    #constitue l'url de la premiere page
    page.url_first = reverse('galerie')
    #on constitue l'url de la derniere page
    page.url_last = reverse('galerie', args = [paginator.num_pages])
    ctx = {'page':page,'paginator':paginator,'photo':photo}
    
    return render_to_response('galerie.html',ctx)

def add_photo(request, *args, **kwargs):
    c = {}
    lie = kwargs["num"]
    per = kwargs["id"]
    act = kwargs['actid']
    obj = kwargs['objid']
    hab = kwargs['habid']
    img = kwargs['img']
    c.update(csrf(request))
    lieu = Lieux.objects.get(id= lie)
    personne = Personne.objects.get(id = per)
    action = Action.objects.get(id = act)
    objet = Objet.objects.get(id= obj)
    habillement = Habillement_bijoux.objects.get(id = hab)
    image = Image_p.objects.get(id = img )
    form = PhotoForm(initial={'lieux':lieu.id ,'personne':personne.id,\
                              'action':action.id,'objet':objet.id,\
                              'habillement':habillement.id ,\
                              'photo':image.id })

    c =({'form':form})
    #~ from ipdb import set_trace; set_trace()
    if request.method == 'POST':
        #~ from ipdb import set_trace; set_trace()
        form = PhotoForm(request.POST,request.FILES)
        #~ from ipdb import set_trace; set_trace()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ajout_lieux'))
        c.update({'form':form})
    c.update(csrf(request))
    return render_to_response('add_photo.html',c)

def delete_confirm_photo (request , *args, **kwargs):
    photo_id = kwargs["num"]
    photo = Photo.objects.get(id = photo_id)
    photo.url = reverse('delete_confirm_photo', args = [photo_id])
    ctx = {'photo':photo}
    return render_to_response('delete_photo.html', ctx )

#~ def deleting_confirm_2 (request , *args , **kwargs):
    #~ photo_id = kwargs["num"]
    #~ photo = Photo.objects.get(id = photo_id)
    #~ return HttpResponseRedirect(reverse('deleting_photo',args =[photo_id]))

def deleting_photo (request , *args, **kwargs):
    photo_id = kwargs["num"]
    photo = Photo.objects.get(id = photo_id)
    photo.delete()
    photos = Photo.objects.all()
    for photo in photos :
        photo.save()
    return HttpResponseRedirect(reverse('info_photo'))
    
def add_image (request,*args, **kwargs):
    c = {}
    lie = kwargs["num"]
    per = kwargs["id"]
    act = kwargs['actid']
    obj = kwargs['objid']
    hab = kwargs['habid']
    c.update(csrf(request))
    form = ImageForm ()
    c.update({'form':form})
    if request.method == 'POST':
        form = ImageForm (request.POST,request.FILES)
        if form.is_valid ():
            #~ from ipdb import set_trace; set_trace()
            form.save()
            id_img = form.instance.id
            #~ from ipdb import set_trace; set_trace()
            return HttpResponseRedirect(reverse('ajoutphoto',\
             args =[int(lie) , int(per) , int(act) ,int(obj) , int(hab) , id_img]))
        c.update({'form':form})
    c.update(csrf(request))
    return render_to_response ('add_image.html', c)


def info_photo (request,*args, **kwargs):
    
    num = kwargs["num"] or 1
    photo = Photo.objects.all()
    paginator = Paginator(photo,15)
    try:
        page = paginator.page(int(num))
        
    except EmptyPage:

        raise Http404
    #s'execute si le numero de la page est 2
    page.is_before_first = (page.number == 2)
    #si le numero de la page est egale au numero de l'avant 
    #de l'anvant dernier
    page.is_before_last = (page.number == paginator.num_pages - 1)
    #on constitue l'url de la page suivante
    page.url_next = reverse('info_photo', args=[int(num) + 1])
    #on constititue l'url de page precedente
    page.url_previous = reverse('info_photo',args=[int(num) - 1])
    #constitue l'url de la premiere page
    page.url_first = reverse('info_photo')
    #on constitue l'url de la derniere page
    page.url_last = reverse('info_photo', args = [paginator.num_pages])
    ctx = {'page':page,'paginator':paginator}
    return render_to_response('info_photo.html',ctx)

def dashphoto (request , *args, **kwargs):
    id_photo = kwargs["num"]
    photo = Photo.objects.get(id =id_photo )
    ctx = {'photo':photo}
    return render_to_response ('dashphoto.html', ctx )


def modif_photo(request , *args, **kwargs):
    ph_id = int(kwargs["id"])
    img_id = kwargs["num"]
    context = {}
    context.update(csrf(request))
    form = modif_photoform ()
    context.update({'form':form})
    photo =  Photo.objects.get(id=ph_id)
    url_image = reverse ('modif_image', args = [photo.photo.id , photo.id])
    data = {}
    if img_id :
        image = Image_p.objects.get(id = img_id)
        data =  {
                    'photographe': photo.photographe.id ,\
                    'theme' : photo.theme.id ,\
                    'format' : photo.format ,\
                    'mode' : photo.mode , \
                    'date' : photo.date ,\
                    'type_p':photo.type_p ,\
                    'personne':photo.personne.id ,\
                    'action' : photo.action.id ,\
                    'photo' : image.id ,\
                    'habillement':photo.habillement.id ,\
                    'objet' : photo.objet.id ,\
                    'lieux' : photo.lieux.id ,\
                    'appareil':photo.appareil ,\
                    'sens' : photo.sens ,\
                    'description': photo.description ,\
                }
    else:
                data =  {
                    'photographe': photo.photographe.id ,\
                    'theme' : photo.theme.id ,\
                    'format' : photo.format ,\
                    'mode' : photo.mode , \
                    'date' : photo.date ,\
                    'type_p':photo.type_p ,\
                    'personne':photo.personne.id ,\
                    'action' : photo.action.id ,\
                    'photo' : photo.photo.id ,\
                    'habillement':photo.habillement.id ,\
                    'objet' : photo.objet.id ,\
                    'lieux' : photo.lieux.id ,\
                    'appareil':photo.appareil ,\
                    'sens' : photo.sens ,\
                    'description': photo.description ,\
                }
    form = modif_photoform (data)
    context.update({'form':form ,'url_image':url_image})
    if request.method == 'POST':
        form = modif_photoform(request.POST,request.FILES)
        photo.photographe_id = request.POST['photographe']
        photo.theme_id =  request.POST['theme']
        photo.format = request.POST['format']
        photo.mode = request.POST['mode']
        photo.date = request.POST['date']
        photo.type_p = request.POST['type_p']
        photo.photo_id = request.POST['photo']
        photo.personne_id = request.POST['personne']
        photo.action_id = request.POST['action']
        photo.habillement_id = request.POST['habillement']
        photo.objet_id = request.POST['habillement']
        photo.lieux_id = request.POST['lieux']
        photo.appareil = request.POST['appareil']
        photo.sens = request.POST['sens']
        photo.description = request.POST['description']
        photo.save ()
        return HttpResponseRedirect(reverse('info_photo'))
    return render_to_response('modif_photo.html',context)

def modif_image (request , *args, **kwargs):
    image_id = kwargs['id']
    modif_id = kwargs["num"]
    context = {}
    context.update(csrf(request))
    image = Image_p.objects.get(id = image_id)
    form = ImageForm    ( initial = {   'title':image.title ,\
                                        'serie':image.serie ,\
                                        'image':image.image 
                                    }
                        )
    context.update({'form':form})
    #~ from ipdb import set_trace; set_trace()
    if request.method == 'POST':
        form = ImageForm (request.POST,request.FILES)
        if form.is_valid ():
            form.save()
            id_img = form.instance.id
            #~ from ipdb import set_trace; set_trace()
            return HttpResponseRedirect (reverse('modif_photo', args =[modif_id , id_img]))
    return render_to_response ('modif_image.html', context)
    
    
def auteur (request):
    
    query = request.GET.get('q', '')
    print query
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(photographe__nom__icontains=query) |
            Q(theme__categorie__icontains = query) |
            Q(theme__theme__nom__icontains = query)
        )
        
        resultat = Photo.objects.filter(qset).distinct()
        #~ from ipdb import set_trace; set_trace()
    else:
        resultat = []
    ctx = {'resultat':resultat , 'query':query}
    return render_to_response('auteur.html',ctx)

def add_autor(request):
    c = {}
    c.update(csrf(request))
    form = Autorform ()
    c.update({'form':form})
    if request.method == 'POST':
        form = Autorform (request.POST)
        data =  {
                    'nom': request.POST['nom'],\
                    'prenom':request.POST['prenom'],\
                    'nationalite':request.POST['nationalite'],\
                    'date1': request.POST['date1'],\
                    'adresse':request.POST['adresse'],\
                    'email':request.POST['email'],\
                    'experience': request.POST['experience'],\
                }

        #~ from ipdb import set_trace; set_trace()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('photographe'))

    c.update({'form':form})
    return render_to_response('add_autor.html', c )
    
def delete_confirm_auteur (request , *args, **kwargs):
    auteur_id = kwargs["num"]
    auteur  = Auteur.objects.get(id = auteur_id)
    ctx = {'auteur':auteur}
    return render_to_response('deleting_auteur.html', ctx)
    
def deleting_auteur (request , *args, **kwargs):
    auteur_id = kwargs["num"]
    auteur  = Auteur.objects.get(id = auteur_id)
    auteur.delete()
    auteurs = Auteur.objects.all()
    for auteur in auteurs :
        auteur.save()
    return HttpResponseRedirect (reverse ('photographe'))

def modif_auteur(request,*args, **kwargs):
    id_autor = kwargs["id"]
    context = {}
    context.update(csrf(request))
    form = Modif_Autorform()
    context.update({'form':form})
    autor = Auteur.objects.get (id = id_autor)
    data = {}
    data =  {   'nom' : autor.nom ,\
                'prenom' : autor.prenom ,\
                'nationalite' : autor.nationalite ,\
                'date1' : autor.date1 ,\
                'adresse' : autor.adresse ,\
                'email' : autor.email ,\
                'experience' : autor.experience ,\
            }
    form = Modif_Autorform (data)
    context.update({'form':form})
    if request.method == 'POST':
        form = Modif_Autorform(request.POST)
        if form.is_valid ():
            autor.nom = request.POST['nom']
            autor.prenom = request.POST['prenom']
            autor.nationalite = request.POST['nationalite']
            autor.date1 = request.POST['date1']
            autor.adresse = request.POST['adresse']
            autor.email = request.POST['email']
            autor.experience = request.POST['experience']
            autor.save()
            return HttpResponseRedirect(reverse('photographe'))
    context.update(csrf(request))
    
    return render_to_response('modif_auteur.html', context)
                
def add_lieux(request):
    context = {}
    context.update(csrf(request))
    form = LieuxForm()
    context.update({'form':form})
    lieu =Lieux()
    if request.method == 'POST':

        lieu.cadre = request.POST.get('cadre') or ''
        lieu.saison =  request.POST.get('saison') or ''
        lieu.type_in = request.POST.get('type_in') or ''
        lieu.type_ex = request.POST.get('type_ex') or ''
        lieu.moment = request.POST.get('moment') or ''
        lieu.pays   = request.POST.get('pays')
        lieu.ville  = request.POST.get('ville')
        doublon = Lieux.objects.filter(cadre = lieu.cadre ,\
                                       saison = lieu.saison ,\
                                       type_in =lieu.type_in ,\
                                       type_ex = lieu.type_ex ,\
                                       moment = lieu.moment ,\
                                       pays = lieu.pays ,\
                                       ville = lieu.ville)

        if not doublon:
            lieu.save()
            return HttpResponseRedirect(reverse('ajout_personne',args =[lieu.id]))
        else:
            a  = doublon[0]
            return HttpResponseRedirect(reverse('ajout_personne',args =[a.id]))

    context.update(csrf(request))    
    return render_to_response('add_lieux.html',context,)

def add_personne(request,*args, **kwargs):
    id_ = kwargs["id"]
    context = {}
    context.update(csrf(request))
    form = PersonneForm ()
    context.update({'form':form})
    personne = Personne()
    if request.method == 'POST':
        personne.sexe = request.POST.get('sexe') or ''
        personne.categorie_dage = request.POST.get('categorie_dage') or ''
        personne.nombre_personne = request.POST.get('nombre_personne') or ''
        personne.prise_de_vue = request.POST.get('prise_de_vue') or ''
        personne.pose = request.POST.get('pose') or ''
        personne.position = request.POST.get('position') or ''
        doublon = Personne.objects.filter (  sexe = personne.sexe,\
                                categorie_dage=personne.categorie_dage,\
                                nombre_personne = personne.nombre_personne,\
                                prise_de_vue = personne.prise_de_vue ,\
                                pose = personne.pose ,\
                                position = personne.position)
        if not doublon:
            personne.save()
            return HttpResponseRedirect(
                reverse('ajout_action',args =[int(id_) ,personne.id]
                       )
                                        )
        else:
            a = doublon[0]
            return HttpResponseRedirect(
                            reverse('ajout_action', args = [id_ ,a.id])
                                        )
    url_lieu = reverse('ajout_lieux')
    context.update({'form':form , 'url_lieu':url_lieu})
    return render_to_response('add_personne.html',context)
    
def add_action(request,*args, **kwargs):
    lie_id = kwargs ['lied']
    per_id = int(kwargs ['persid'])
    context = {}
    context.update(csrf(request))
    form = ActionForm ()
    context.update({'form':form})
    action = Action()
    if request.method == 'POST':
        action.action_personnage = request.POST.get('action_personnage') or ''
        action.type_pose = request.POST.get('type_pose') or ''
        action.Cadre_action = request.POST.get('Cadre_action') or ''
        doublon = Action.objects.filter(
                        action_personnage=action.action_personnage,\
                                        type_pose = action.type_pose,\
                                        Cadre_action = action.Cadre_action)
        if not doublon :
            action.save()
            return HttpResponseRedirect(
                    reverse(
            'ajout_objet', args=[int(lie_id) , int(per_id) , action.id]
                            )
                            )
        else:
            a = doublon[0]
            return HttpResponseRedirect (reverse('ajout_objet',\
                            args=[int(lie_id) , int(per_id) , a.id]))
        
    context.update({'form':form})
    return render_to_response ('add_action.html',context)
    
def add_objet(request,*args, **kwargs):
    lie_id = kwargs ['lied']
    per_id = kwargs ['persid']
    act_id = kwargs ['actid']
    context = {}
    context.update(csrf(request))
    form = ObjetForm ()
    context.update({'form':form})
    objet = Objet()
    if request.method == 'POST':
        objet.objet_naturel = request.POST.get('objet_naturel') or ''
        objet.objet_fabrique = request.POST.get('objet_fabrique') or ''
        objet.objet_domestique = request.POST.get('objet_domestique') or ''
        objet.objet_travail = request.POST.get('objet_travail') or ''
        objet.vehicule  = request.POST.get ('vehicule') or ''
        objet.objet_loisir = request.POST.get('objet_loisir') or ''
        objet.objet_decoratif = request.POST.get('objet_decoratif') or ''
        doublon = Objet.objects.filter(objet_naturel=objet.objet_naturel,\
                                    objet_fabrique=objet.objet_fabrique,\
                                    objet_domestique=objet.objet_domestique,\
                                    objet_travail = objet.objet_travail ,\
                                    vehicule = objet.vehicule , \
                                    objet_loisir=objet.objet_loisir, \
                                    objet_decoratif = objet.objet_decoratif)
        if not doublon:
            objet.save()
            return HttpResponseRedirect(reverse
            ('ajout_habit',\
             args=[int(lie_id) , int(per_id) , int(act_id) , objet.id]))
        else:
            a = doublon[0]
            return HttpResponseRedirect (reverse
            ('ajout_habit',\
            args=[int(lie_id) , int(per_id) , int(act_id) ,a.id])
                        )
    context.update({'form':form})
    return render_to_response ('add_objet.html',context)
                                    
def add_habillement(request,*args, **kwargs):
    lie_id = kwargs ['lied']
    per_id = kwargs ['persid']
    act_id = kwargs ['actid']
    obj_id = kwargs ['objid']
    context = {}
    context.update(csrf(request))
    form = HabillementForm ()
    context.update({'form':form})
    habit = Habillement_bijoux()
    if request.method == 'POST':
        habit.habillement = request.POST.get('habillement') or ''
        habit.type_habillement = request.POST.get('type_habillement') or ''
        habit.Vetement = request.POST.get('Vetement') or ''
        habit.chaussures = request.POST.get('chaussures') or ''
        habit.bijoux = request.POST.get('bijoux') or ''
        habit.coiffe = request.POST.get('coiffe') or ''
        doublon= Habillement_bijoux.objects.filter(habillement=habit.habillement,\
                                            type_habillement= habit.type_habillement,\
                                            Vetement = habit.Vetement ,\
                                            chaussures = habit.chaussures , \
                                            bijoux = habit.bijoux ,\
                                            coiffe = habit.coiffe)
        if not doublon:
            habit.save()
            return HttpResponseRedirect(reverse
            ('image',\
             args=[int(lie_id) , int(per_id) , int(act_id) ,int(obj_id) , habit.id]))
        else:
            a = doublon[0]
            return HttpResponseRedirect (reverse
            ('image',\
            args=[int(lie_id) , int(per_id) , int(act_id) ,int(obj_id), a.id]))
    context.update({'form':form})
    return render_to_response ('add_habit.html',context)
