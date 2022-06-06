from django.shortcuts import render,redirect 




def home(request):
    return render(request,"home.html", {"home": home})

def services(request):
    return render(request,"services.html", {"services": services})


   