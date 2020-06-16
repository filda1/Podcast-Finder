from django.shortcuts import render, HttpResponse

def Interviews(request):
    #return HttpResponse("Welcome")
    return render(request,'interviews.html', {})