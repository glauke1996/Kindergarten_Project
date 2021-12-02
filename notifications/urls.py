from django.urls import path
from . import views

app_name = "notifications"

urlpatterns = [
    path("", views.BoardView, name="notifications"),
    path("<int:pk>/", views.post_detail, name="detail"),
    path("<int:pk>/photos/", views.PostPhotosView.as_view(), name="photos"),
    path(
        "<int:post_pk>/photos/<int:photo_pk>/edit/",
        views.EditPhotoView.as_view(),
        name="edit-photo",
    ),
    path(
        "<int:post_pk>/photos/<int:photo_pk>/delete/",
        views.delete_photo,
        name="delete-photo",
    ),
    path(
        "<int:pk>/photos/create/",
        views.AddPhotoView.as_view(),
        name="create-photo",
    ),
    path(
        "post/create/",
        views.UploadPostView.as_view(),
        name="create-post",
    ),
    path("search/", views.search, name="search"),
]
