from django.shortcuts import render, HttpResponse

def Best(request):
    #return HttpResponse("Welcome")
    return render(request,'bestpodcasts.html', {})