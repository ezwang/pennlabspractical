from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^card$", views.add_card_view, name="add_card"),
    url(r"^card/(?P<cardId>\d+)", views.view_delete_card_view, name="view_card"),

    url(r"^list$", views.add_list_view, name="add_list"),
    url(r"^list/(?P<listId>\d+)$", views.view_delete_list_view, name="view_list"),
    url(r"^editlist/(?P<listId>\d+)$", views.edit_list_view, name="edit_list"),
]
