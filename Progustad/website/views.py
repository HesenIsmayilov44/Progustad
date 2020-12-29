from django.shortcuts import render

# Create your views here.

def home(request):
    content = {
        'title':'HomePage'
    }
    return render(request,'homePage.html',content)