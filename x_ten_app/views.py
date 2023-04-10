from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,"jsp.html")


def about(request):
    return render(request,"about.html")


def ourvalue(request):
    return render(request,"our.html")



def service(request):
    return render(request,"service.html")



def weding(request):
    return render(request,"wedding.html")
