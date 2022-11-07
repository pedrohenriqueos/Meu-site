from django.shortcuts import render 
import firebase_admin
from .conf.settings import CERTIFICATE,DATABASEURL

cred = firebase_admin.credentials.Certificate(CERTIFICATE)
default_app = firebase_admin.initialize_app(cred, {
	'databaseURL': DATABASEURL
	})

def home(request): 
    #teste = db.reference('teste').get()
    #valor = db.reference('valor').get()
    #name = db.reference('obj/name').get()
    #return render(request,"Home.html",{"teste":teste,"valor":valor,"name":name })
    return render(request,"Home.html",{'header':"Principal"})