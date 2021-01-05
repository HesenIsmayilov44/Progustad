from django.shortcuts import render

# Create your views here.
def challenges(request):
    return render(request,'challenges.html')

def challengeDetail(request,id):
    content = {
        'id':id
    }
    return render(request,'challengeDetail.html',content)

