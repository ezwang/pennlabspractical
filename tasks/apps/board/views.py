from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import F

from .models import List, Card


def add_card_view(request):
    if not request.method == "POST":
        return JsonResponse({"error": "The only allowed methods for this endpoint are POST."}, status=405)

    listId = request.POST.get("listId")
    title = request.POST.get("title")
    description = request.POST.get("description", "")

    if not listId or not title:
        return JsonResponse({"error": "Missing list ID and title in card creation request."}, status=400)

    try:
        listId = int(listId)
    except ValueError:
        return JsonResponse({"error": "Could not parse list ID."}, status=400)

    try:
        ls = get_object_or_404(List, id=listId)
    except Http404:
        return JsonResponse({"error": "Invalid list ID! A list with that ID does not exist."}, status=400)

    card = Card.objects.create(title=title, description=description, ls=ls)
    return JsonResponse({"success": True, "id": card.id})


def view_delete_card_view(request, cardId):
    try:
        card = get_object_or_404(Card, id=cardId)
    except Http404:
        return JsonResponse({"error": "The card you are trying to retrieve/modify does not exist!"}, status=404)

    if request.method == "DELETE":
        card.delete()
        return JsonResponse({"success": True})
    elif request.method == "GET":
        return JsonResponse({
            "title": card.title,
            "description": card.description,
            "listId": card.ls.id
        })
    else:
        return JsonResponse({"error": "The only allowed methods for this endpoint are GET, DELETE."}, status=405)


def add_list_view(request):
    if not request.method == "POST":
        return JsonResponse({"error": "The only allowed methods for this endpoint are POST."}, status=405)

    title = request.POST.get("title")

    if not title:
        return JsonResponse({"error": "Missing title in list creation request."}, status=400)

    ls = List.objects.create(title=title, order=List.objects.all().count() + 1)

    return JsonResponse({"success": True, "id": ls.id})


def view_delete_list_view(request, listId):
    try:
        ls = get_object_or_404(List, id=listId)
    except Http404:
        return JsonResponse({"error": "The list you are trying to retrieve/modify does not exist!"}, status=404)

    if request.method == "DELETE":
        List.objects.filter(order__gt=ls.order).update(order=F("order") - 1)
        ls.delete()
        return JsonResponse({"success": True})
    elif request.method == "GET":
        return JsonResponse({"title": ls.title, "order": ls.order})
    else:
        return JsonResponse({"error": "The only allowed methods for this endpoint are GET, DELETE."}, status=405)


def edit_list_view(request, listId):
    try:
        ls = get_object_or_404(List, id=listId)
    except Http404:
        return JsonResponse({"error": "The list you are trying to retrieve/modify does not exist!"}, status=404)

    title = request.POST.get("title")
    order = request.POST.get("order")

    if title:
        ls.title = title

    if order:
        try:
            order = int(order)
        except ValueError:
            return JsonResponse({"error": "Unable to parse list order!"}, status=400)

        List.objects.filter(order__gt=ls.order).update(order=F("order") - 1)
        List.objects.filter(order__gte=order).update(order=F("order") + 1)
        ls.order = order

    ls.save()
    return JsonResponse({"success": True})
