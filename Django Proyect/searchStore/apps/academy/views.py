from django.shortcuts import render, HttpResponse

def Academy(request):
    #return HttpResponse("Welcome")
    return render(request,'academy.html', {})