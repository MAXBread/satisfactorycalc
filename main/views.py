from django.shortcuts import render
from .sandbox import SandBox


def home(request):
    sandbox = SandBox(request=request)
    if request.POST:
        if 'btn-tablet' in request.POST:
            print('btn-tab')
            sandbox.add()
        elif 'btn-newprint' in request.POST:
            print('btn-new')
            print(sandbox.sandbox)
        elif 'btn-delete' in request.POST:
            print('btn-del')
    print(sandbox.sandbox)
    return render(request, 'main/index.html', context={'sandbox': sandbox})
