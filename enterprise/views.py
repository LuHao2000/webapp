from django.shortcuts import render

# Create your views here.
def tomessage(request):
    return render(request, 'sims/message.html')

def toinfo(request):
    return render(request, 'enterprise/info.html')

def torelease(request):
    return render(request, 'enterprise/release.html')


def tocontent(request):
    return render(request, 'enterprise/content.html')

def torelated(request):
    return render(request, 'enterprise/related.html')

def toindex(request):
    return render(request, 'enterprise/index.html')

def toinfo_edit(request):
     return render(request, 'enterprise/info-edit.html')


def tostanderd(request):
    return render(request, 'enterprise/standard.html')

