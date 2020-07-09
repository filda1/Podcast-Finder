from django.shortcuts import render, HttpResponse

def Explorer(request):
    #return HttpResponse("Welcome")
    return render(request,'explorer.html', {})