from django.shortcuts import render, HttpResponse

def Allepisodes(request):
    #return HttpResponse("Welcome")
    return render(request,'episodes/allepisodes.html', {})