from django.db import models


class Card(models.Model):
    title = models.TextField()
    order = models.IntegerField()


class List(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True)
    listId = models.ForeignKey("List", on_delete=models.CASCADE)
