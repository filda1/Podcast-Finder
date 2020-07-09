from django.shortcuts import render, HttpResponse

def Readmoreacademy(request):
    #return HttpResponse("Welcome")
    return render(request,'readmoreacademy.html', {})