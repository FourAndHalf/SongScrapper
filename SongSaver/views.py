from django.shortcuts import render

def startup_page(request):
    return render(request, 'SongSaver/link.html')
