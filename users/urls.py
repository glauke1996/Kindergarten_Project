from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("profile/<int:pk>/", views.ProfileView, name="profile"),
    path("profile/<int:user_pk>/update/", views.UpdateProfileView.as_view(), name="update"),
]
