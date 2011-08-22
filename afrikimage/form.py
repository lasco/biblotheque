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



class PersonneForm(forms.ModelForm):
    sexe = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset= Categorie_personne.objects.filter(az = 'sexe'),required=False)
    categorie_dage = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset= Categorie_personne.objects.filter(az = 'categorie_dage'),required=False )
    nombre_personne = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset= Categorie_personne.objects.filter(az = 'nombre_personne'),required=False )
    prise_de_vue = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset= Categorie_personne.objects.filter(az = 'prise_de_vue'),required=False )
    pose = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset= Categorie_personne.objects.filter(az = 'pose'),required=False)
    position = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset= Categorie_personne.objects.filter(az = 'position'),required=False )
    class Meta:
        model = Personne


a_checkboxchoice1 = [['immobile','immobile'],['en mouvement','en mouvement']]
a_checkboxchoice2 = [['Photo posee','Photo posée'],['Photo prise sur le vif','Photo prise sur le vif']]
a_checkboxchoice3 = [['travail','travail'],['etude','etude'],['vie quotidienne','vie quotidienne'],['loisir','loisir']]

class ActionForm (forms.Form):
    action_personnage = forms.ChoiceField (label=u"action du personnage" ,required=False, widget=RadioSelect(), choices= a_checkboxchoice1)
    type_pose  = forms.ChoiceField(label='type de pose',widget=RadioSelect(),choices = a_checkboxchoice2 ,required=False)
    Cadre_action = forms.ChoiceField(label="Cadre de l\'action",widget=RadioSelect(),choices = a_checkboxchoice3 ,required=False)




class ObjetForm(forms.ModelForm):

    objet_naturel = forms.ModelMultipleChoiceField (widget=forms.CheckboxSelectMultiple(), queryset= Categorie_objet.objects.filter( type_objet = 'objet_naturel'),required=False)
    objet_fabrique = forms.ModelMultipleChoiceField (widget=forms.CheckboxSelectMultiple(), queryset= Categorie_objet.objects.filter( type_objet = 'objet_fabrique'),required=False)
    objet_domestique = forms.ModelMultipleChoiceField (widget=forms.CheckboxSelectMultiple(), queryset= Categorie_objet.objects.filter( type_objet = 'objet_domestique'),required=False)
    objet_travail = forms.ModelMultipleChoiceField (widget=forms.CheckboxSelectMultiple(), queryset= Categorie_objet.objects.filter( type_objet = 'objet_travail'),required=False)
    vehicule = forms.ModelMultipleChoiceField ( widget=forms.CheckboxSelectMultiple(), queryset= Categorie_objet.objects.filter( type_objet = 'vehicule'),required=False)
    objet_loisir =  forms.ModelMultipleChoiceField (widget=forms.CheckboxSelectMultiple(), queryset= Categorie_objet.objects.filter( type_objet = 'objet_loisir'),required=False)
    objet_decoratif =  forms.ModelMultipleChoiceField (widget=forms.CheckboxSelectMultiple(), queryset= Categorie_objet.objects.filter( type_objet = 'objet_decoratif'),required=False)
    class Meta:
        model = Objet

class HabillementForm (forms.ModelForm):
    habillement = forms.ModelMultipleChoiceField (widget=forms.CheckboxSelectMultiple(), queryset= Categorie_habit.objects.filter( type_habit = 'habillement'),required=False)
    type_habillement =  forms.ModelMultipleChoiceField (widget=forms.CheckboxSelectMultiple(), queryset= Categorie_habit.objects.filter( type_habit = 'type_habillement'),required=False)
    Vetement =  forms.ModelMultipleChoiceField (widget=forms.CheckboxSelectMultiple(), queryset= Categorie_habit.objects.filter( type_habit = 'Vetement'),required=False)
    chaussures = forms.ModelMultipleChoiceField (widget=forms.CheckboxSelectMultiple(), queryset= Categorie_habit.objects.filter( type_habit = 'chaussures'),required=False)
    bijoux = forms.ModelMultipleChoiceField (widget=forms.CheckboxSelectMultiple(), queryset= Categorie_habit.objects.filter( type_habit = 'bijoux'),required=False)
    coiffe = forms.ModelMultipleChoiceField (widget=forms.CheckboxSelectMultiple(), queryset= Categorie_habit.objects.filter( type_habit = 'coiffe'),required=False)
    class Meta:
        model = Habillement_bijoux
