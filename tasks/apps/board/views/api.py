from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import F

from ..models import List, Card


def add_card_view(request):
    """ The API endpoint for adding a card. """
    if not request.method == "POST":
        return JsonResponse({"status": 405, "error": "The only allowed methods for this endpoint are POST."}, status=405)

    listId = request.POST.get("listId")
    title = request.POST.get("title")
    description = request.POST.get("description", "")

    if not listId or not title:
        return JsonResponse({"status": 400, "error": "Missing list ID and title in card creation request."}, status=400)

    try:
        listId = int(listId)
    except ValueError:
        return JsonResponse({"status": 400, "error": "Could not parse list ID."}, status=400)

    try:
        ls = get_object_or_404(List, id=listId)
    except Http404:
        return JsonResponse({"status": 400, "error": "Invalid list ID! A list with that ID does not exist."}, status=400)

    card = Card.objects.create(title=title, description=description, ls=ls)
    return JsonResponse({"status": 200, "id": card.id})


def all_card_view(request):
    """ The API endpoint for listing all of the cards. """
    cards = Card.objects.all()
    output = []

    for card in cards:
        output.append({
            "id": card.id,
            "title": card.title,
            "description": card.description,
            "listId": card.ls.id
        })

    return JsonResponse({"status": 200, "cards": output})


def all_list_view(request):
    """ The API endpoint for listing all of the lists. """
    lists = List.objects.all().order_by("order")
    output = []

    for ls in lists:
        output.append({
            "id": ls.id,
            "title": ls.title,
            "order": ls.order
        })

    return JsonResponse({"status": 200, "lists": output})


def view_list_cards_view(request, listId):
    """ The API endpoint for viewing cards associated with a list after given a list ID. """
    try:
        ls = get_object_or_404(List, id=listId)
    except Http404:
        return JsonResponse({"status": 404, "error": "The list you are trying to retrieve does not exist!"}, status=404)

    if request.method == "GET":
        output = []

        for card in ls.card_set.all():
            output.append({
                "id": card.id,
                "title": card.title,
                "description": card.description
            })

        return JsonResponse({"status": 200, "cards": output})
    else:
        return JsonResponse({"status": 405, "error": "The only allowed methods for this endpoint is GET."}, status=405)


def view_delete_card_view(request, cardId):
    """ The API endpoint for viewing, modifying, and deleting cards. """
    try:
        card = get_object_or_404(Card, id=cardId)
    except Http404:
        return JsonResponse({"status": 404, "error": "The card you are trying to retrieve/modify does not exist!"}, status=404)

    if request.method == "DELETE":
        # Deleting a Card
        card.delete()
        return JsonResponse({"status": 200})
    elif request.method == "GET":
        # Viewing a Card
        return JsonResponse({
            "title": card.title,
            "description": card.description,
            "listId": card.ls.id
        })
    elif request.method == "POST":
        # Editing a Card
        title = request.POST.get("title")
        description = request.POST.get("description")
        listId = request.POST.get("listId")

        if title:
            card.title = title

        # Allow for description to be empty
        if description is not None:
            card.description = description

        if listId:
            try:
                listId = int(listId)
            except ValueError:
                return JsonResponse({"status": 400, "error": "Unable to parse new list ID!"}, status=400)

            try:
                ls = get_object_or_404(List, id=listId)
            except Http404:
                return JsonResponse({"status": 404, "error": "The list you are trying to retrieve does not exist!"}, status=404)

            card.ls = ls

        card.save()

        return JsonResponse({"status": 200})
    else:
        return JsonResponse({"status": 405, "error": "The only allowed methods for this endpoint are GET, POST, DELETE."}, status=405)


def add_list_view(request):
    """ The API endpoint for adding a list. """
    if not request.method == "POST":
        return JsonResponse({"status": 405, "error": "The only allowed methods for this endpoint are POST."}, status=405)

    title = request.POST.get("title")

    if not title:
        return JsonResponse({"status": 400, "error": "Missing title in list creation request."}, status=400)

    # Create the list and put it at the end of the board.
    ls = List.objects.create(title=title, order=List.objects.all().count() + 1)

    return JsonResponse({"status": 200, "id": ls.id})


def view_delete_list_view(request, listId):
    """ The API endpoint for viewing and deleting lists. """
    try:
        ls = get_object_or_404(List, id=listId)
    except Http404:
        return JsonResponse({"status": 404, "error": "The list you are trying to retrieve/modify does not exist!"}, status=404)

    if request.method == "DELETE":
        # Shift all lists after the current list back one.
        List.objects.filter(order__gt=ls.order).update(order=F("order") - 1)
        ls.delete()
        return JsonResponse({"status": 200})
    elif request.method == "GET":
        return JsonResponse({"title": ls.title, "order": ls.order})
    else:
        return JsonResponse({"status": 405, "error": "The only allowed methods for this endpoint are GET, DELETE."}, status=405)


def edit_list_view(request, listId):
    """ The API endpoint for editing a list. """
    if not request.method == "POST":
        return JsonResponse({"status": 405, "error": "The only allowed methods for this endpoint are POST."}, status=405)

    try:
        ls = get_object_or_404(List, id=listId)
    except Http404:
        return JsonResponse({"status": 404, "error": "The list you are trying to retrieve/modify does not exist!"}, status=404)

    title = request.POST.get("title")
    order = request.POST.get("order")

    if title:
        ls.title = title

    if order:
        try:
            order = int(order)
        except ValueError:
            return JsonResponse({"status": 400, "error": "Unable to parse list order!"}, status=400)

        # Remove the list from the order (shift all lists after it back one).
        List.objects.filter(order__gt=ls.order).update(order=F("order") - 1)

        # Add the list to the order (shift all lists after it forward one).
        List.objects.filter(order__gte=order).update(order=F("order") + 1)

        ls.order = order

    ls.save()
    return JsonResponse({"status": 200})
