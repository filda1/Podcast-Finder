from django.shortcuts import render, HttpResponse

def Realtime(request):
    #return HttpResponse("Welcome")
    return render(request,'realtime.html', {})