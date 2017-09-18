from django.conf.urls import url

from .views import frontend, api

urlpatterns = [
    # Frontend
    url(r"^$", frontend.index_view, name="index"),

    # Card API Endpoints
    url(r"^card$", api.add_card_view, name="add_card"),
    url(r"^card/(?P<cardId>\d+)$", api.view_delete_card_view, name="view_card"),
    url(r"^card/all$", api.all_card_view, name="view_card_all"),

    # List API Endpoints
    url(r"^list$", api.add_list_view, name="add_list"),
    url(r"^list/(?P<listId>\d+)$", api.view_delete_list_view, name="view_list"),
    url(r"^list/(?P<listId>\d+)/cards$", api.view_list_cards_view, name="view_list_cards"),
    url(r"^list/all$", api.all_list_view, name="view_list_all"),
    url(r"^editlist/(?P<listId>\d+)$", api.edit_list_view, name="edit_list"),
]
