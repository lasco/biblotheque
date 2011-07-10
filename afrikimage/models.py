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

class Personne (models.Model):
    sexe = models.CharField(max_length =40 , blank = True,\
                                choices = (('Homme','Homme'),
                                           ('Femme','Femme')))
    categorie_dage = models.CharField(max_length=20 ,blank = True,\
                                verbose_name = u"categorie d\'âge",\
                                choices = (('Enfant','Enfant'),
                                            ('Adolescent','Adolescent'),
                                            ('Adulte','Adulte'),
                                    ( u'ersonne âgé',u'personne âgé')))
    nombre_personne = models.CharField(max_length=15,blank = True,\
                                verbose_name = u'nombre de personnes',\
                                    choices = (('1','1'),
                                      ('Entre 2 et 5','Entre 2 et 5'),
                                      ('Entre 6 et 10','Entre 6 et 10'),
                                    ('Entre 10 et 20','Entre 10 et 20'),
                                    ('Plus de 20','Plus de 20')))
    prise_de_vue = models.CharField(max_length=20,blank = True,\
                                    verbose_name = u'prise de vue',\
                                    choices = (('Entier','Entier'),
                                (u'plan americain',u'plan américain'),
                                ('Portrait','Portrait'),
                                ('gros plan','gros plan')))
    pose = models.CharField (max_length=15, blank = True,\
                            choices=(('de face','de face'),
                            ('de profil','de profil'),
                            ('de dos','de dos'),
                            ('de trois quart','de trois quart')))
    position = models.CharField (max_length=15, blank = True, \
                                  choices=(('debout','débout'),
                                         ('Assis','Assis'),
                                         ('couche',u'couché')))
    def __unicode__(self):

        return '%s-%s-%s ' %(self.sexe ,self.pose,self.position) 
                                        
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

class Objet (models.Model):
    objet_naturel = models.CharField (max_length = 15 , blank = True,
                                      verbose_name = 'objet naturel',\
                                      choices = (('animal','animal'),
                                                 ('vegetal','vegetal')))
    objet_fabrique = models.CharField(max_length = 15 , blank = True,\
                                    verbose_name = 'objet fabrique',\
                                choices=(('Manufacturé','Manufacturé'),
                                        ('industriel','industriel')))
    objet_domestique = models.CharField(max_length = 40 , blank = True,\
                                      verbose_name='objet domestique',\
              choices=(
                        ('ustensile de cuisine','ustensile de cuisine'),
                        ('entretien du corps' , 'entretien du corps'),
                        ('mobilier' , 'mobilier'),
                        ('luminaire','luminaire'),
                        ('menage' , 'menage'),
                        ('bibelot' , 'bibelot'),
                        ('Appareil électrique ou électronique','Appareil électrique ou électronique'),
                        ('Outil de communication','Outil de communication')))
    objet_travail = models.CharField (max_length=10 ,blank= True , \
                                    verbose_name = 'objet de travail',\
                                    choices = (('outil','outil'),
                                                ('Machine','Machine')))
    vehicule = models.CharField ( max_length=20 , blank=True ,\
                                    verbose_name = 'Véhicule' ,\
                                    choices = (('Vélo','Vélo'),
                                              ('Moto, mobylette','Moto, mobylette'),
                                              ('Voiture','Voiture'),
                                              ('Camion','Camion'),
                                              ('Bus','Bus')))
    objet_loisir = models.CharField ( max_length = 30 , blank = True,\
                                verbose_name='objet de loisir',\
                                choices=(('Jeu  jouet','Jeu jouet'),
                                          ('equipement sportif','equipement sportif'),
                                          ('instrument de musique','instrument de musique')))
    objet_decoratif = models.CharField ( max_length = 15 , blank=True ,\
                                        verbose_name  = 'objet décoratif',\
                                        choices = (('Objet d’art','Objet d’art '),
                                                    ('Objet artisanal','Objet artisanal')))

    def __unicode__(self):
        return '%s-%s-%s-%s-%s-%s-%s'%(self.objet_naturel,self.objet_fabrique,self.objet_domestique,self.objet_travail,self.vehicule,self.objet_loisir,self.objet_decoratif)

class Habillement_bijoux (models.Model):
    habillement = models.CharField(max_length=8 , blank = True,\
                                    choices =(('nu','nu'),
                                              ('habille','habille')))
    type_habillement = models.CharField(max_length=20, blank = True,\
                                verbose_name = "type d\'habillement",\
                                choices = (('traditionnel','Traditionnel'),
                                        ('moderne','moderne'),
                            ('tenue de mariage','tenue de mariage'),
                            ('tenue de fête','tenue de fête')))
    Vetement  = models.CharField (max_length= 25 , blank = True, \
                                    verbose_name ='vêtement',\
                                            choices=(('boubou','boubou'),
                                                ('complet','complet'),
                                                ('robe','robe'),
                                                ('jupe','jupe'),
                                                ('pantalon','pantalon'),
                                                ('tunique','tunique'),
                                                ('chemise','chemise'),
                                                ('haut à manches courtes','haut à manches courtes'),
                                                ('haut à manches longues','haut à manches longues'),
                                                ('haut sans manches','haut sans manches')))
    chaussures = models.CharField(max_length = 25 , blank = True ,\
                                    choices =(('Pieds nus','Pieds nus'),
                                               ('sandales','sandales'),
                                               ('ballerines','ballerines'),
                                               ('chaussures fermées','chaussures fermées'),
                                               ('escarpins','escarpins'),
                                               ('chaussures à talons','chaussures à talons'),
                                               ('mules, tongs','mules, tongs'),
                                               ('bottes','bottes'),
                                               ('baskets, tennis','baskets, tennis')))
    bijoux  = models.CharField (max_length =20 , blank = True, \
                                    choices=(('Collier','Collier'),
                                             ('boucles d oreilles',"boucles d\'oreilles"),
                                             ('bracelet','bracelet'),
                                             ('tour de cheville','tour de cheville'),
                                             ('sautoir','sautoir'),
                                             ('montre','montre'),
                                             ('bague','bague')))
    coiffe = models.CharField (max_length = 20 ,blank = True , \
                                    choices = (('chapeau ','chapeau '),
                                               ('casquette','casquette'),
                                               ('béret','béret'),
                                               ('foulard','foulard'),
                                               ('autre coiffe','autre coiffe')))
    def __unicode__(self):
        
        return "%s-%s-%s-%s-%s-%s" %(self.habillement,self.type_habillement,self.Vetement,self.chaussures,self.bijoux,self.coiffe)



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
    type_p=models.CharField(max_length=10,
                                verbose_name="Type de prise de vue",
                            choices=(('A','Argentique'),
                                     ('N','Numerique')))
    personne = models.ForeignKey(Personne)
    action = models.ForeignKey(Action)
    habillement = models.ForeignKey(Habillement_bijoux)
    objet = models.ForeignKey(Objet)
    photo = models.ForeignKey(Image_p)
    lieux = models.ForeignKey(Lieux)
    appareil = models.CharField(max_length=20,blank=True ,\
                                verbose_name=u"Appareil utilise")
    sens = models.CharField(max_length=20,choices=(('Horizontale','Horizontale'),
                                                    ('Horizontale','Verticale'),
                                                    ('Carree','Carree')))
    description = models.TextField(max_length=70,blank=True)
    def __unicode__(self):
        return "% s  %s " % (self.photographe , self.theme)

admin.site.register(Auteur)
admin.site.register(Theme)
admin.site.register(Categorie)
admin.site.register(Lieux)
admin.site.register(Photo)
admin.site.register(Image_p)
admin.site.register(Personne)
admin.site.register(Action)
admin.site.register(Objet)
admin.site.register(Habillement_bijoux)
