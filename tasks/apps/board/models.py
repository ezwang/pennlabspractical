from django.db import models


class List(models.Model):
    title = models.TextField()
    order = models.IntegerField()


class Card(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True)
    listId = models.ForeignKey(List, null=True, on_delete=models.CASCADE)
