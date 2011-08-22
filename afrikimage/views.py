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
    form = PhotoForm()
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
    
    # formatage des index
    #index personne
    
    index_pers = [persexe['name'] for persexe in photo.personne.sexe.values()]
    index_pers2 =[percategorie_dage['name'] for percategorie_dage in photo.personne.categorie_dage.values()]
    index_pers3 = [pernombre_personne['name'] for pernombre_personne in photo.personne.nombre_personne.values()]
    index_pers4 = [perprise_de_vue['name'] for perprise_de_vue in photo.personne.prise_de_vue.values()]
    index_pers5 = [perpose['name'] for perpose in photo.personne.pose.values()]
    index_pers6 = [perposition['name'] for perposition in photo.personne.position.values()]
    index_pers.extend(index_pers2)
    index_pers.extend(index_pers3)
    index_pers.extend(index_pers4)
    index_pers.extend(index_pers5)
    index_pers.extend(index_pers6)
    
    # index habilllement et bijoux
    
    index_habit =  [hab_habillement['name'] for hab_habillement in photo.habillement.habillement.values()]
    index_habit2 = [hab_type_habillement['name'] for hab_type_habillement in photo.habillement.type_habillement.values()]
    index_habit3 = [hab_Vetement['name'] for hab_Vetement in photo.habillement.Vetement.values()]
    index_habit4 = [hab_chaussures['name'] for hab_chaussures in photo.habillement.chaussures.values()]
    index_habit5 = [hab_bijoux['name'] for hab_bijoux in photo.habillement.bijoux.values()]
    index_habit6 = [hab_coiffe['name'] for hab_coiffe in photo.habillement.coiffe.values()]
    index_habit.extend(index_habit2)
    index_habit.extend(index_habit3)
    index_habit.extend(index_habit4)
    index_habit.extend(index_habit5)
    index_habit.extend(index_habit6)
    
    # index object 
    
    index_obj = [obj_objet_naturel['name'] for obj_objet_naturel in photo.objet.objet_naturel.values()]
    index_obj2 = [obj_objet_fabrique['name'] for obj_objet_fabrique in photo.objet.objet_fabrique.values()]
    index_obj3 = [obj_objet_domestique['name'] for obj_objet_domestique in photo.objet.objet_domestique.values()]
    index_obj4 = [obj_objet_travail['name'] for obj_objet_travail in photo.objet.objet_travail.values()]
    index_obj5 = [obj_vehicule['name'] for obj_vehicule in photo.objet.vehicule.values()]
    index_obj6 = [obj_objet_loisir['name'] for obj_objet_loisir in photo.objet.objet_loisir.values()]
    index_obj7 = [obj_objet_decoratif['name'] for obj_objet_decoratif in photo.objet.objet_decoratif.values()]
    index_obj.extend(index_obj2)
    index_obj.extend(index_obj3)
    index_obj.extend(index_obj4)
    index_obj.extend(index_obj5)
    index_obj.extend(index_obj6)
    index_obj.extend(index_obj7)
    

    
    ctx = {'photo':photo , 'index_pers':index_pers,\
                        'index_habit':index_habit,\
                        'index_obj':index_obj ,\
                        }
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
    # si l'id de l'image existe on remplace cet id par celle de la photo
    # existante
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
                print photo.personne.id
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
                    'objet' :photo.objet.id  ,\
                    'lieux' : photo.lieux.id ,\
                    'appareil':photo.appareil ,\
                    'sens' : photo.sens ,\
                    'description': photo.description ,\
                }
                
    form = modif_photoform (data)
    context.update({'form':form ,'url_image':url_image})
    if request.method == 'POST':
        form = modif_photoform(request.POST,request.FILES)
        if form.is_valid():
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
            photo.objet_id = request.POST['objet']
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
    if query:
        qset = (
            Q(photo__title__icontains=query) |
            Q(photographe__nom__icontains=query) |
            Q(theme__categorie__icontains = query) |
            Q(theme__theme__nom__icontains = query) |
            Q(mode__icontains = query) |
            Q(sens__icontains = query) |
            Q(date__icontains = query) |
            Q(description__icontains = query)
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
        form = PersonneForm (request.POST)
        if form.is_valid():
            persexe = request.POST.get('sexe')
            percategorie_dage = request.POST.get('categorie_dage') 
            pernombre_personne = request.POST.get('nombre_personne')
            perprise_de_vue = request.POST.get('prise_de_vue')
            perpose = request.POST.get('pose')
            perposition = request.POST.get('position')
            doublon = Personne.objects.filter (  sexe = persexe,\
                                    categorie_dage=percategorie_dage,\
                                    nombre_personne = pernombre_personne,\
                                    prise_de_vue = perprise_de_vue ,\
                                    pose = perpose ,\
                                    position = perposition)
            if not doublon:
                
                form.save()
                return HttpResponseRedirect(reverse('ajout_action',args =[int(id_) ,form.instance.id]))
            else:
                a = doublon[0]
                return HttpResponseRedirect(
                                reverse('ajout_action', args = [id_ ,a.id])
                                        )
    context.update({'form':form })
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
    if request.method == 'POST':
        form = ObjetForm (request.POST)
        objet = Objet()
        if form.is_valid():
            obj_naturel = request.POST.get ('objet_naturel')
            obj_fabrique = request.POST.get ('objet_fabrique')
            obj_domestique = request.POST.get ('objet_domestique')
            obj_travail = request.POST.get ('objet_travail')
            vehicule  = request.POST.get ('vehicule')
            obj_loisir = request.POST.get ('objet_loisir')
            obj_decoratif = request.POST.get('objet_decoratif')
            doublon = Objet.objects.filter(objet_naturel= obj_naturel,\
                                    objet_fabrique= obj_fabrique ,\
                                    objet_domestique = obj_domestique,\
                                    objet_travail = obj_travail ,\
                                    vehicule = vehicule , \
                                    objet_loisir= obj_loisir, \
                                    objet_decoratif = obj_decoratif)
            if not doublon:
                form.save()
                return HttpResponseRedirect(reverse
                            ('ajout_habit',\
             args=[int(lie_id) , int(per_id) , int(act_id) ,form.instance.id]))
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
    if request.method == 'POST':
        form = HabillementForm(request.POST)
        if form.is_valid():
            habillement = request.POST.get('habillement')
            type_habillement = request.POST.get('type_habillement')
            Vetement = request.POST.get('Vetement')
            chaussures = request.POST.get('chaussures')
            bijoux = request.POST.get('bijoux')
            coiffe = request.POST.get('coiffe')
            doublon= Habillement_bijoux.objects.filter(habillement=habillement,\
                                            type_habillement= type_habillement,\
                                            Vetement = Vetement ,\
                                            chaussures = chaussures , \
                                            bijoux = bijoux ,\
                                            coiffe = coiffe)
            if not doublon:
                form.save()
                return HttpResponseRedirect(reverse
                    ('image',\
             args=[int(lie_id) , int(per_id) , int(act_id) ,int(obj_id) , form.instance.id]))
            else:
                a = doublon[0]
                return HttpResponseRedirect (reverse
                        ('image',\
                args=[int(lie_id) , int(per_id) , int(act_id) ,int(obj_id), a.id]))
    context.update({'form':form})
    return render_to_response ('add_habit.html',context)


def search_lieu (request):
    context = {}
    context.update(csrf(request))
    form = LieuxForm()
    context.update({'form':form})
    if request.method == 'POST':
        cadre = request.POST.get('cadre') or ''
        print cadre
        saison = request.POST.get('saison') or ''
        type_in = request.POST.get('type_in') or ''
        type_ex = request.POST.get('type_ex') or ''
        moment = request.POST.get('moment')  or ''
        pays = request.POST.get('pays') or ''
        ville  = request.POST.get('ville') or ''
        response = Photo.objects.filter(lieux__cadre = cadre , \
                                        lieux__saison = saison , \
                                        lieux__type_in = type_in , \
                                        lieux__type_ex = type_ex , \
                                        lieux__moment = moment , \
                                        lieux__pays = pays ,\
                                        lieux__ville = ville )
                                        
        context.update( {'response':response} )
    context.update(csrf(request))
    return render_to_response ('search_lieu.html' , context )
    
def search_action (request):
    context = {}
    context.update(csrf(request))
    form = ActionForm ()
    context.update({'form':form})
    if request.method == 'POST':
        action_personnage = request.POST.get('action_personnage') or ''
        print action_personnage
        type_pose = request.POST.get('type_pose') or ''
        Cadre_action = request.POST.get('Cadre_action') or ''
        response = Photo.objects.filter (action__action_personnage = action_personnage , \
                        action__type_pose = type_pose , \
                        action__Cadre_action  = Cadre_action )
        print response
        context.update( {'response':response} )
    context.update(csrf(request))
    return render_to_response ( 'search_action.html', context )
    
def search_personne (request):
    context = {}
    context.update(csrf(request))
    form = PersonneForm ()
    context.update({'form':form})
    if request.method == 'POST':
        form = PersonneForm (request.POST)
        if form.is_valid():
            sexe = request.POST.get('sexe')
            categorie_dage = request.POST.get('categorie_dage')
            nombre_personne = request.POST.get('nombre_personne')
            prise_de_vue = request.POST.get('prise_de_vue')
            pose = request.POST.get('pose') 
            position = request.POST.get('position')
            response = Photo.objects.filter (personne__sexe = sexe ,\
                                    personne__categorie_dage = categorie_dage,\
                                    personne__nombre_personne = nombre_personne,\
                                    personne__prise_de_vue = prise_de_vue ,\
                                    personne__pose = pose ,\
                                    personne__position = position)
            print response
            context.update( {'response':response} )
        context.update(csrf(request))
    
    return render_to_response ('search_personne.html', context )

def search_habit (request):
    context = {}
    context.update(csrf(request))
    form = HabillementForm ()
    context.update({'form':form})
    if request.method == 'POST':
        form = HabillementForm(request.POST)
        if form.is_valid():
            habillement = request.POST.get('habillement')
            type_habillement = request.POST.get('type_habillement')
            Vetement = request.POST.get('Vetement')
            chaussures = request.POST.get('chaussures')
            bijoux = request.POST.get('bijoux')
            coiffe = request.POST.get('coiffe')
            response = Photo.objects.filter(habillement__habillement = habillement,\
                                            habillement__type_habillement = type_habillement,\
                                            habillement__Vetement = Vetement ,\
                                            habillement__chaussures = chaussures , \
                                            habillement__bijoux = bijoux ,\
                                            habillement__coiffe = coiffe)
            print response
            context.update( {'response':response} )
        context.update(csrf(request))
    return render_to_response ('search_habit.html' , context )

def search_objet (request):
    context = {}
    context.update(csrf(request))
    form = ObjetForm ()
    context.update({'form':form})
    if request.method == 'POST':
        form = ObjetForm (request.POST)
        objet = Objet()
        if form.is_valid():
            obj_naturel = request.POST.get ('objet_naturel')
            obj_fabrique = request.POST.get ('objet_fabrique')
            obj_domestique = request.POST.get ('objet_domestique')
            obj_travail = request.POST.get ('objet_travail')
            vehicule  = request.POST.get ('vehicule')
            obj_loisir = request.POST.get ('objet_loisir')
            obj_decoratif = request.POST.get('objet_decoratif')
            response = Photo.objects.filter(objet__objet_naturel= obj_naturel,\
                                    objet__objet_fabrique= obj_fabrique ,\
                                    objet__objet_domestique = obj_domestique,\
                                    objet__objet_travail = obj_travail ,\
                                    objet__vehicule = vehicule , \
                                    objet__objet_loisir= obj_loisir, \
                                    objet__objet_decoratif = obj_decoratif)
            context.update( {'response':response} )
        context.update(csrf(request))
    return render_to_response ('search_objet.html' , context )
    

