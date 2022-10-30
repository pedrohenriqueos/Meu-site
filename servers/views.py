from django.shortcuts import render

def servers(request): 
    return render(request,"Server.html")