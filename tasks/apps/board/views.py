from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404

from .models import List, Card


def add_card_view(request):
    pass


def view_delete_card_view(request, cardId):
    try:
        card = get_object_or_404(Card, id=cardId)
    except Http404:
        return JsonResponse({"error": "The card you are trying to retrieve/modify does not exist!"}, status=404)

    if request.method == "DELETE":
        card.delete()
        return JsonResponse({"success": True})

    return JsonResponse({
        "title": card.title,
        "description": card.description,
        "listId": card.ls.id
    })


def add_list_view(request):
    pass


def view_delete_list_view(request, listId):
    try:
        ls = get_object_or_404(List, id=listId)
    except Http404:
        return JsonResponse({"error": "The list you are trying to retrieve/modify does not exist!"}, status=404)

    if request.method == "DELETE":
        ls.delete()
        return JsonResponse({"success": True})

    return JsonResponse({"title": ls.title, "order": ls.order})


def edit_list_view(request, listId):
    try:
        ls = get_object_or_404(List, id=listId)
    except Http404:
        return JsonResponse({"error": "The list you are trying to retrieve/modify does not exist!"}, status=404)
    pass
