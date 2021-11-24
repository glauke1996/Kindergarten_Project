from django.urls import path
from . import views
from notifications import views

app_name = "comments"

urlpatterns = [
    # path("create/<int:pk>", views.create_comment, name="create"),
    path("create/comment/", views.post_detail, name="create-comment"),
]
