from django.urls import path
from . import views

app_name = "comments"

urlpatterns = [
    path("create/<int:pk>", views.create_comment, name="create"),
]
