from django.db import models


class List(models.Model):
    """
    Represents a list object.

    Attributes:
        title - The title of the list.
        order - The order of the list, ranging from 1 to the total number of lists (inclusive).
    """

    title = models.TextField()
    order = models.IntegerField()


class Card(models.Model):
    """
    Represents a card object.

    Attributes:
        title - The title of the card.
        description - The card description (optional, can be blank).
        ls - The list that this card is attached to. Use ls.id for the list ID.
    """

    title = models.TextField()
    description = models.TextField(blank=True)
    ls = models.ForeignKey(List, null=True, on_delete=models.CASCADE)
