from django.shortcuts import render, HttpResponse

def Hot(request):
    #return HttpResponse("Welcome")
    return render(request,'hot.html', {})