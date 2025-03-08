from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>/", views.view_post, name="view_post"),
    path("new", views.new_post, name="new_post"),
]
