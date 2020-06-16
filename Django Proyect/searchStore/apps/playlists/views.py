from django.shortcuts import render, HttpResponse

def Playlists(request):
    #return HttpResponse("Welcome")
    return render(request,'playlists.html', {})