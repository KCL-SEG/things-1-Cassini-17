from django.shortcuts import render

def things_page(request):
    return render(request, 'page.html')



