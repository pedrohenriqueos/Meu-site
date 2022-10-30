from django.shortcuts import render 
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

# cred = credentials.Certificate(".firebase/mysite-pedro-firebase-adminsdk-6upkf-a3497584f5.json")
# app  = firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://mysite-pedro-default-rtdb.firebaseio.com'
# })

def home(request): 
    #teste = db.reference('teste').get()
    #valor = db.reference('valor').get()
    #name = db.reference('obj/name').get()
    #return render(request,"Home.html",{"teste":teste,"valor":valor,"name":name })
    return render(request,"Home.html",{'header':"Principal"})