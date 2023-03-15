from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':120}
    return render(request,'conditions.html',context=d)

def conditions1(request):
    d={'a':100,'b':120}
    return render(request,'conditions1.html',context=d)

def conditions2(request):
    d={'a':50,'b':70,'c':60}
    return render(request,'conditions2.html',context=d)

def conditions3(request):
    d={'a':43,'b':50,'c':55}
    return render(request,'conditions3.html',context=d)

