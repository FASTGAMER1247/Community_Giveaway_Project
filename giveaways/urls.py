from django.urls import path
from . import views

urlpatterns = [
    path("new/", views.create_item, name="create_item"),
    path("<int:pk>/", views.item_detail, name="item_detail"),
    path("<int:pk>/claim/", views.claim_item, name="claim_item"),
    path("<int:pk>/mark-available/", views.mark_available, name="mark_available"),
    path("mine/", views.my_items, name="my_items"),
]
