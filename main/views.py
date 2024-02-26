from django.shortcuts import render

from .models import Recipe, Item
from .sandbox import SandBox


def home(request):
    sandbox = SandBox(request=request)
    if request.POST:
        if 'btn-tablet' in request.POST:
            print('btn-tab')
            sandbox.add()
        elif 'btn-recipe-list' in request.POST:
            print('btn-recipe-list')
        elif 'btn-delete' in request.POST:
            print('btn-del')
            sandbox.delete()
        else:
            for item in sandbox.sandbox:
                if f"btn-question-{item['id']}" in request.POST:
                    print(f"btn-question-{item['id']}")
                    sandbox.activate(question_id=item['id'])
                    break

    items = Item.objects.all()
    return render(request, 'main/index.html', context={'items': items, 'sandbox': sandbox})
