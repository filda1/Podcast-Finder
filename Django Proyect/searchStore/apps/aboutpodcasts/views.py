from django.shortcuts import render, HttpResponse

def Aboutpodcasts(request):
    #return HttpResponse("Welcome")
    return render(request,'aboutpodcasts.html', {})