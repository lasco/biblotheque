#!/usr/bin/env python
# -*- coding= UTF-8 -*-

from django.db import models
from django.contrib import admin

class Auteur(models.Model):
    """
    Table photographe
    """
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    nationalite = models.CharField(max_length=30)
    date1 = models.CharField (max_length=10,\
                                verbose_name='date de naissance', \
                                        blank=True)
    adresse = models.TextField (max_length=90 , blank=True)
    email = models.EmailField ( blank=True )
    experience= models.TextField(max_length=80, blank=True)
    
    list_display = ('nom','prenom')
    
    def __unicode__(self):
        return "%s %s" % (self.nom,self.prenom)
        
class Theme (models.Model):
    """
    Table theme
    """
    nom = models.CharField (max_length = 50,verbose_name='Thematique')
    
    def __unicode__(self):
        return '%s' % self.nom

class Categorie (models.Model):
    """
    table categorie
    """
    theme = models.ForeignKey (Theme)
    categorie = models.CharField (max_length= 80)
    def __unicode__(self):
        return '%s : %s' % (self.theme , self.categorie)

class Categorie_personne(models.Model):

    az = models.CharField(max_length = 50 , verbose_name = "type")
    name = models.CharField(max_length= 50 ) 

    def __unicode__(self):
        return "%s" % self.name

class Personne (models.Model):
    sexe = models.ManyToManyField(Categorie_personne ,blank = True , related_name = 'sexe' )
    categorie_dage = models.ManyToManyField(Categorie_personne ,blank = True , related_name = 'categorie_dage' )
    nombre_personne = models.ManyToManyField(Categorie_personne ,blank = True , related_name = 'nombre_personne' )
    prise_de_vue = models.ManyToManyField(Categorie_personne ,blank = True , related_name = 'prise_de_vue' )
    pose = models.ManyToManyField(Categorie_personne ,blank = True , related_name = 'pose' )
    position = models.ManyToManyField(Categorie_personne ,blank = True , related_name = 'position' )


class Lieux(models.Model):

    cadre = models.CharField (max_length=15, blank=True,\
                                choices= (('Interieur','Interieur'),
                                         ('Exterieur','Exterieur'))
                             )
    saison = models.CharField   (max_length=15,blank=True,\
                            choices= (('saison froide','saison froide'),
                                      ('saison chaude','saison chaude'),
                                    ('saison des pluies','saison des pluies'))
                                )
    type_in =models.CharField   (max_length=15,blank=True,\
                                    verbose_name="type d'interieur",\
                                    choices= (('Maison','Maison'),
                                              ('Bureau','Bureau'),
                                              ('Studio','Studio'),
                                              ('Autre','Autre'))
                                )
    type_ex =models.CharField   (   max_length=15, blank = True,\
                                    verbose_name="type d'exterieur",\
                                        choices=(('Ville','Ville'),
                                                ('Village','Village'),
                                                ('Nature','Nature'))
                                )
    moment = models.CharField (max_length = 6 , blank = True ,\
                                        choices = (('jour','jour'),
                                                    ('nuit','nuit')))
    pays = models.CharField (max_length = 15 )
    ville = models.CharField (max_length = 15 )
    
    def __unicode__(self):
        return "%s-%s-%s-%s-%s-%s-%s " %(self.cadre, self.saison, self.type_in , self.type_ex , self.moment , self.pays , self.ville)

class Action (models.Model):
    action_personnage = models.CharField(max_length=20,blank = True,\
                        verbose_name ='action du personnage',\
                        choices=(('immobile','immobile'),
                                 ('en mouvement','en mouvement')))
    type_pose = models.CharField(max_length=20,blank = True,\
                                verbose_name='type de pose',\
                                choices=(('Photo posee','Photo posée'),
                ('Photo prise sur le vif','Photo prise sur le vif')))
    Cadre_action = models.CharField(max_length=20,blank = True,\
                                    verbose_name= "Cadre de l\'action",\
                                choices=(('travail','travail'),
                                ('etude','etude'),
                                ('vie quotidienne','vie quotidienne'),
                                ('loisir','loisir')))
    def __unicode__(self):
        return '%s-%s-%s' %(self.action_personnage , self.type_pose, self.Cadre_action)

class Categorie_objet(models.Model):
    type_objet =  models.CharField(max_length = 50 )
    name =  models.CharField(max_length = 50 )
    def __unicode__(self):
        return "%s" % self.name

class Objet (models.Model):
    objet_naturel =  models.ManyToManyField(Categorie_objet ,blank = True , related_name = 'objet_naturel' )
    objet_fabrique = models.ManyToManyField(Categorie_objet ,blank = True , related_name = 'objet_fabrique' )
    objet_domestique = models.ManyToManyField(Categorie_objet ,blank = True , related_name = 'objet_domestique' )
    objet_travail = models.ManyToManyField(Categorie_objet ,blank = True , related_name = 'objet_travail' )
    vehicule = models.ManyToManyField(Categorie_objet ,blank = True , related_name = 'vehicule' )
    objet_loisir =  models.ManyToManyField(Categorie_objet ,blank = True , related_name = 'objet_loisir' )
    objet_decoratif =  models.ManyToManyField(Categorie_objet ,blank = True , related_name = 'objet_decoratif' )


class Categorie_habit(models.Model):
    type_habit = models.CharField(max_length = 50 )
    name =     models.CharField(max_length = 50 )
    def __unicode__(self):
        return "%s" % self.name

class Habillement_bijoux (models.Model):
    habillement = models.ManyToManyField(Categorie_habit ,blank = True , related_name = 'habillement' )
    type_habillement = models.ManyToManyField(Categorie_habit ,blank = True , related_name = 'type_habillement' )
    Vetement  = models.ManyToManyField(Categorie_habit ,blank = True , related_name = 'Vetement' )
    chaussures = models.ManyToManyField(Categorie_habit ,blank = True , related_name = 'chaussures' )
    bijoux  = models.ManyToManyField(Categorie_habit ,blank = True , related_name = 'bijoux' )
    coiffe =  models.ManyToManyField(Categorie_habit ,blank = True , related_name = 'coiffe' )


class Image_p (models.Model):
    title = models.CharField(max_length=25 ,verbose_name = "Titre" , blank = True)
    serie = models.CharField(max_length=50 ,verbose_name = "série", blank = True)
    image = models.ImageField(upload_to="photos/")
    thumbnail = models.ImageField(upload_to="thumbnails/", editable=False)

    def save(self):
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        import os 

        # Set our max thumbnail size in a tuple (max width, max height)
        THUMBNAIL_SIZE = (500,500)

        # Ouvre la photo originale en utilisant la librairie PIL

        image = Image.open(self.image)

        # convertir l'mage en mode RGB si necessaire
        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')

        # Utilisation de PIL Image pour creer un thumbnail
        # has a thumbnail() convenience method that contrains proportions.
        # Additionally, we use Image.ANTIALIAS to make the image look better.
        # Without antialiasing the image pattern artifacts may result.
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        # sauvegarde du thumbnail 
        temp_handle = StringIO()
        image.save(temp_handle, 'JPEG')
        temp_handle.seek(0)

        # sauvegarde du champ thumbnail

        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                temp_handle.read(), content_type='image/JPEG')
        self.thumbnail.save(suf.name+'.JPEG', suf, save=False)
        # Sauvegarde de l'instance photo
        super(Image_p , self).save()
    def __unicode__(self):
        return "%s  %s" % (self.title , self.serie)

class Photo(models.Model):
    """
    Table Image 
    """
    photographe = models.ForeignKey(Auteur)
    theme = models.ForeignKey(Categorie)
    format = models.CharField(max_length = 10)
    mode = models.CharField(max_length =10 , choices=(('N/B','N/B'),
                                                      ('Couleur','Couleur')))
    date = models.CharField (max_length=10,verbose_name='date de prise de vue')
    type_p =  models.CharField(max_length=10,
                                verbose_name="Type de prise de vue",
                            choices=(('A','argentique'),
                                     ('N','numerique')))
    personne = models.ForeignKey(Personne)
    action = models.ForeignKey(Action)
    habillement = models.ForeignKey(Habillement_bijoux)
    objet = models.ForeignKey(Objet)
    photo = models.ForeignKey(Image_p)
    lieux = models.ForeignKey(Lieux)
    appareil = models.CharField(max_length=20,blank=True ,\
                                verbose_name=u"Appareil utilise")
    sens = models.CharField(max_length=20,choices=(('horizontale','horizontale'),
                                                    ('verticale','verticale'),
                                                    ('carree','carree')))
    description = models.TextField(max_length=70,blank=True)
    def __unicode__(self):
        return "% s  %s " % (self.photographe , self.theme)


admin.site.register(Auteur)
admin.site.register(Theme)
admin.site.register(Categorie)
admin.site.register(Lieux)
admin.site.register(Photo)
admin.site.register(Image_p)
admin.site.register(Categorie_personne)
admin.site.register(Personne)
admin.site.register(Action)
admin.site.register(Categorie_objet)
admin.site.register(Objet)
admin.site.register(Categorie_habit)
admin.site.register(Habillement_bijoux)
