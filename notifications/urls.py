from django.urls import path
from . import views

app_name = "notifications"

urlpatterns = [
    path("", views.BoardView.as_view(), name="notifications"),
    path("<int:pk>/", views.post_detail, name="detail"),
    path("<int:pk>/photos/", views.PostPhotosView.as_view(), name="photos"),
    path(
        "<int:post_pk>/photos/<int:photo_pk>/edit/",
        views.EditPhotoView.as_view(),
        name="edit-photo",
    ),
    path("search/", views.search, name="search"),
]
