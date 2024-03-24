from django.contrib import admin
from main.models import Recipe, Item, Fabric, VariantInput, VariantOutput


@admin.register(Fabric)
class FabricImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'fabric_image')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'item_image')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'fabric', 'base_item')


@admin.register(VariantInput)
class VariantInputAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')


@admin.register(VariantOutput)
class VariantOutputAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')
