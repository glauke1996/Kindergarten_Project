from django.urls import path
from . import views

app_name = "notifications"

urlpatterns = [
    path("", views.BoardView.as_view(), name="notifications"),
    path("<int:pk>", views.post_detail, name="detail"),
]
