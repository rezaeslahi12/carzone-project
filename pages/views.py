from django.shortcuts import render

def home_views(request):
    return render(request,'pages/home.html')