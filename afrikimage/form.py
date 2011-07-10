#!/usr/bin/env python
# -*- coding= UTF-8 -*-

from models import *
from PIL import Image
import datetime

from django import forms
from django.forms.widgets import RadioSelect , CheckboxSelectMultiple
from django.forms.fields import MultipleChoiceField

class SearchForm(forms.Form):
    recherche = forms.CharField(max_length=50)
    
class PhotoForm(forms.ModelForm):
    DATE_FORMAT = '%d/%m/%y'
    class Meta:
        model = Photo

class ImageForm (forms.ModelForm):
    class Meta:
        model = Image_p

class modif_photoform(forms.ModelForm):
    DATE_FORMAT = '%d/%m/%y'
    class Meta:
        model = Photo


class Autorform(forms.ModelForm):
    DATE_FORMAT = '%d/%m/%y'
    
    class Meta:
        model = Auteur


class Modif_Autorform(forms.Form):
    
    DATE_FORMAT = '%d/%m/%Y'
    
    nom = forms.CharField(max_length = 30)
    prenom = forms.CharField(max_length = 30)
    nationalite = forms.CharField(max_length = 30)
    date1 = forms.CharField(label = 'Date de naissance')
    adresse = forms.CharField(max_length = 200,required=False)
    email = forms.EmailField (required=False)
    experience = forms.CharField (max_length = 200 , required=False)


checkboxchoice1 =  [['Interieur','Interieur'],['Exterieur','Exterieur']]
checkboxchoice2 = [['saison froide','saison froide'],['saison chaude','saison chaude'],['saison des pluies','saison des pluies']]
checkboxchoice3 = [['Maison','Maison'],['Bureau','Bureau'],['Studio','Studio'],['Autre','Autre']]
checkboxchoice4 = [['Ville','Ville'],['Village','Village'],['Nature','Nature']]
checkboxchoice5 = [['jour','jour'],['nuit','nuit']]

class LieuxForm(forms.Form):

    
    cadre = forms.ChoiceField(widget=RadioSelect(),choices=checkboxchoice1 , required=False)
    saison = forms.ChoiceField(widget=RadioSelect(),choices=checkboxchoice2 ,required=False)
    type_in = forms.ChoiceField(label='Type d interieur',widget=RadioSelect(),choices=checkboxchoice3 ,required=False)
    type_ex = forms.ChoiceField(label='Type d exterieur',widget=RadioSelect(),choices=checkboxchoice4 ,required=False)
    moment = forms.ChoiceField(widget=RadioSelect(),choices=checkboxchoice5 ,required=False)
    pays = forms.CharField (max_length = 15)
    ville = forms.CharField (max_length = 15)
p_checkboxchoice1 = (('Homme','Homme'),('Femme','Femme'))
p_checkboxchoice2 = (('Enfant','Enfant'),('Adolescent','Adolescent'),('Adulte','Adulte'),( u'ersonne âgé',u'personne âgé'))
p_checkboxchoice3 = [[('1 p'),('1')],['Entre 2 et 5','Entre 2 et 5'],['Entre 6 et 10','Entre 6 et 10'],['Entre 10 et 20','Entre 10 et 20'],['Plus de 20','Plus de 20']]
p_checkboxchoice4 = (('Entier','Entier'),(u'plan americain',u'plan américain'),('Portrait','Portrait'),('gros plan','gros plan'))
p_checkboxchoice5 = (('de face','de face'),('de profil','de profil'),('de dos','de dos'),('de trois quart','de trois quart'))
p_checkboxchoice6 = (('debout','debout'),('Assis','Assis'),('couche',u'couché'))

class PersonneForm(forms.Form):
    sexe = forms.MultipleChoiceField (required=False,widget=CheckboxSelectMultiple(), choices= p_checkboxchoice1)
    categorie_dage = forms.MultipleChoiceField (label=u"categorie d\'age",required=False,widget=CheckboxSelectMultiple(), choices= p_checkboxchoice2)
    nombre_personne = forms.MultipleChoiceField(label='nombre de personne',widget=RadioSelect(),choices = p_checkboxchoice3 ,required=False)
    prise_de_vue = forms.MultipleChoiceField(label='prise de vue',widget=CheckboxSelectMultiple(),choices = p_checkboxchoice4 ,required=False)
    pose = forms.MultipleChoiceField(widget=CheckboxSelectMultiple(),choices = p_checkboxchoice5 ,required=False)
    position = forms.MultipleChoiceField(widget=RadioSelect(),choices = p_checkboxchoice6 ,required=False)
    
a_checkboxchoice1 = [['immobile','immobile'],['en mouvement','en mouvement']]
a_checkboxchoice2 = [['Photo posee','Photo posée'],['Photo prise sur le vif','Photo prise sur le vif']]
a_checkboxchoice3 = [['travail','travail'],['etude','etude'],['vie quotidienne','vie quotidienne'],['loisir','loisir']]

class ActionForm (forms.Form):
    action_personnage = forms.ChoiceField (label=u"action du personnage" ,required=False, widget=RadioSelect(), choices= a_checkboxchoice1)
    type_pose  = forms.ChoiceField(label='type de pose',widget=RadioSelect(),choices = a_checkboxchoice2 ,required=False)
    Cadre_action = forms.ChoiceField(label="Cadre de l\'action",widget=RadioSelect(),choices = a_checkboxchoice3 ,required=False)
    

o_checkboxchoice1 = (('animal','animal'),('vegetal','vegetal'))
o_checkboxchoice2 = (('manufacture','manufacture'),('industriel','industriel'))
o_checkboxchoice3 = (('ustensile de cuisine','ustensile de cuisine'),('entretien du corps' , 'entretien du corps'),('mobilier' , 'mobilier'),('luminaire','luminaire'),('menage' , 'menage'),('bibelot' , 'bibelot'),('Appareil électrique ou électronique','Appareil électrique ou électronique'),('Outil de communication','Outil de communication'))
o_checkboxchoice5 = (('outil','outil'),('Machine','Machine'))
o_checkboxchoice6 = (('Vélo','Vélo'),('Moto, mobylette','Moto, mobylette'),('Voiture','Voiture'),('Camion','Camion'),('Bus','Bus'))
o_checkboxchoice4 = (('Jeu  jouet','Jeu jouet'),('equipement sportif','equipement sportif'),('instrument de musique','instrument de musique'))
o_checkboxchoice7 = (('Objet d’art','Objet d’art '),('Objet artisanal','Objet artisanal'))

class ObjetForm(forms.Form):

    objet_naturel = forms.ChoiceField (label=u"objet naturel",required=False,widget=CheckboxSelectMultiple(), choices= o_checkboxchoice1)
    objet_fabrique = forms.ChoiceField (label=u"objet fabriqué",required=False,widget=CheckboxSelectMultiple(), choices= o_checkboxchoice2)
    objet_domestique = forms.ChoiceField (label=u"objet domestique",required=False,widget=CheckboxSelectMultiple(), choices= o_checkboxchoice3)
    objet_travail = forms.ChoiceField (label=u"objet de travail",required=False,widget=CheckboxSelectMultiple(), choices= o_checkboxchoice5)
    vehicule = forms.ChoiceField (label=u"véhicule",required=False,widget=CheckboxSelectMultiple(), choices= o_checkboxchoice6)
    objet_loisir = forms.ChoiceField (label=u"objet de loisir",required=False,widget=CheckboxSelectMultiple(), choices= o_checkboxchoice4)
    objet_decoratif = forms.ChoiceField (label=u"objet decoratif",required=False,widget=CheckboxSelectMultiple(), choices= o_checkboxchoice7)
    
h_checkboxchoice1 = (('nu','nu'),('habille','habille'))
h_checkboxchoice2 = (('traditionnel','Traditionnel'),('moderne','moderne'),('tenue de mariage','tenue de mariage'),('tenue de fête','tenue de fête'))
h_checkboxchoice3 = (('boubou','boubou'),('complet','complet'),('robe','robe'),('jupe','jupe'),('pantalon','pantalon'),('tunique','tunique'),('chemise','chemise'),('haut à manches courtes','haut à manches courtes'),('haut à manches longues','haut à manches longues'),('haut sans manches','haut sans manches'))
h_checkboxchoice4 = (('Collier','Collier'),('boucles d oreilles',"boucles d\'oreilles"),('bracelet','bracelet'),('tour de cheville','tour de cheville'),('sautoir','sautoir'),('montre','montre'),('bague','bague'))
h_checkboxchoice5 = (('Pieds nus','Pieds nus'),('sandales','sandales'),('ballerines','ballerines'),('chaussures fermées','chaussures fermées'),('escarpins','escarpins'),('chaussures à talons','chaussures à talons'),('mules, tongs','mules, tongs'),('bottes','bottes'),('baskets, tennis','baskets, tennis'))
h_checkboxchoice6 = (('chapeau ','chapeau '),('casquette','casquette'),('béret','béret'),('foulard','foulard'),('autre coiffe','autre coiffe'))
class HabillementForm (forms.Form):
    habillement = forms.ChoiceField (required=False,widget=CheckboxSelectMultiple(), choices= h_checkboxchoice1)
    type_habillement =  forms.ChoiceField (label=u"type d\'habillement",required=False,widget=CheckboxSelectMultiple(), choices= h_checkboxchoice2)
    Vetement =  forms.ChoiceField (label=u"vêtement",required=False,widget=CheckboxSelectMultiple(), choices= h_checkboxchoice3)
    chaussures = forms.ChoiceField (required=False ,widget=CheckboxSelectMultiple() , choices= h_checkboxchoice5 )
    bijoux = forms.ChoiceField (required=False,widget=CheckboxSelectMultiple(), choices= h_checkboxchoice4)
    coiffe = forms.ChoiceField (required=False,widget=CheckboxSelectMultiple(), choices= h_checkboxchoice6)
