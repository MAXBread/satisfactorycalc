from django import template
from main.models import Fabric, Item

register = template.Library()


@register.simple_tag
def factory_image_url(factory_id: int):
    factory = Fabric.objects.get(id=factory_id)
    return factory.fabric_image.url


@register.simple_tag
def item_image_url(item_id: int):
    item = Item.objects.get(id=item_id)
    return item.item_image.url
