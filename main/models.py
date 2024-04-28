from django.db import models


class Fabric (models.Model):
    name = models.CharField(max_length=30, db_index=True, unique=True)
    fabric_image = models.ImageField(upload_to='icons/fabrics')
    # TODO: fabric > factory

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=30, db_index=True, unique=True)
    item_image = models.ImageField(upload_to='icons/items')

    def __str__(self):
        return self.name


class VariantInput(models.Model):
    product = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'


class VariantOutput(models.Model):
    product = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'


class Recipe (models.Model):
    name = models.CharField(max_length=30, db_index=True, unique=True)
    fabric = models.ForeignKey(Fabric, on_delete=models.SET_NULL, null=True)
    input = models.ManyToManyField(VariantInput, blank=True)
    output = models.ManyToManyField(VariantOutput, blank=True)
    base_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # TODO: fabric > factory

    def __str__(self):
        return self.name
