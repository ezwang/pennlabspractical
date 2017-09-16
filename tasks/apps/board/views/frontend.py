from django.shortcuts import render


def index_view(request):
    """ The frontend for the API. """

    return render(request, "index.html")
