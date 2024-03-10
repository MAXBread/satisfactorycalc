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
            for block in sandbox.product_line:
                if f"btn-question-{block.block_id}" in request.POST:
                    print(f"btn-question-{block.block_id}")
                    sandbox.activate(block_id=block.block_id)
                    break
            for item in items:
                if f"item-{item.id}" in request.POST:
                    print(f"item-{item.id}")
                    print(item.name)
                    recipe = Recipe(name=item.name)
                    # sandbox.add_recipe(recipe=recipe)
                    break

    return render(request, 'main/index.html', context={'items': items, 'sandbox': sandbox})
