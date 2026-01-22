"""Defines URL patters for Accounts."""

from django.urls import path, include

app_name = "accounts"  # ignore pylint: disable=invalid-name

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
]
