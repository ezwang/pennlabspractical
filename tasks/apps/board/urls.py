from django.conf.urls import url

from .views import frontend, api

urlpatterns = [
    url(r"^card$", api.add_card_view, name="add_card"),
    url(r"^card/(?P<cardId>\d+)", api.view_delete_card_view, name="view_card"),

    url(r"^list$", api.add_list_view, name="add_list"),
    url(r"^list/(?P<listId>\d+)$", api.view_delete_list_view, name="view_list"),
    url(r"^editlist/(?P<listId>\d+)$", api.edit_list_view, name="edit_list"),
]
