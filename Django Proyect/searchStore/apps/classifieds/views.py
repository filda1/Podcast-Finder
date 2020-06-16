from django.shortcuts import render, HttpResponse

def Classifieds(request):
    #return HttpResponse("Welcome")
    return render(request,'classifieds.html', {})