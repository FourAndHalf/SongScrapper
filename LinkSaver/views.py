from django.shortcuts import render
from .models import FormData

def link(request):
    return render(request, 'link.html')

def link_saved_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        link = request.POST.get('link')

    print("Name:", name)
    print("Title:", title)
    print("Link:", link)
    
    FormData.objects.create(name=name, title=title, link=link)

    return render(request, 'data_saved.html')