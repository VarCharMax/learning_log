"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = "learning_logs"  # ignore pylint: disable=invalid-name
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Page that shows all topics.
    path("topics/", views.topics, name="topics"),
    path("topics/<int:topic_id>/", views.topic, name="topic"),
]
