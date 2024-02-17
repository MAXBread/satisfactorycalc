from django.shortcuts import render


def home(request):
    if request.POST:
        if 'btn-tablet' in request.POST:
            print('btn-tab')
        elif 'btn-newprint' in request.POST:
            print('btn-new')
        elif 'btn-delete' in request.POST:
            print('btn-del')
    return render(request,'main/index.html')
