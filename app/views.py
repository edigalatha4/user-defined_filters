from django.shortcuts import render

# Create your views here.

def usd(request):
    d={'data':'hello goodmorning!!'}
    return render(request,'usd.html',d)

    
