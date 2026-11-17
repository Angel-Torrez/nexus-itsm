from django.urls import path
from django.utils.module_loading import import_string
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path(
        "register/",
        import_string("apps.authentication.views.RegisterView").as_view(),
        name="auth-register",
    ),
    path("login/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path(
        "me/",
        import_string("apps.authentication.views.UserDetailView").as_view(),
        name="auth-me",
    ),
]