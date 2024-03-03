from django.shortcuts import render

from .models import Recipe, Item
from .sandbox import SandBox


def home(request):
    sandbox = SandBox(request=request)
    items = Item.objects.all()
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
            for item in sandbox.product_line:
                if f"btn-question-{item['block_id']}" in request.POST:
                    print(f"btn-question-{item['block_id']}")
                    sandbox.activate(question_id=item['block_id'])
                    break
            for item in items:
                if f"item-{item.id}" in request.POST:
                    print(f"item-{item.id}")
                    print(item.name)
                    break


    return render(request, 'main/index.html', context={'items': items, 'sandbox': sandbox})
