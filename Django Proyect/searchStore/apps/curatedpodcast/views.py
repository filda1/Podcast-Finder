from django.shortcuts import render, HttpResponse

def Curated(request):
    #return HttpResponse("Welcome")
    return render(request,'curatedpodcasts.html', {})