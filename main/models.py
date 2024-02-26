from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=20, db_index=True, unique=True)
    image = models.ImageField(upload_to='icons/items')


class Recipe (models.Model):
    name = models.CharField(max_length=20, db_index=True, unique=True)
    image = models.ImageField(upload_to='icons/items')
