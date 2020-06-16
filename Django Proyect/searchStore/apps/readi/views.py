from django.shortcuts import render, HttpResponse

def Readi(request):
    #return HttpResponse("Welcome")
    return render(request,'readi.html', {})