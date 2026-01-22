"""_summary_

Returns:
    _type_: _description_
"""

from django.http import HttpResponse
from django.shortcuts import render
from .models import Topic


def index(request) -> HttpResponse:
    """The home page for Learning Log."""
    return render(request, "learning_logs/index.html")


def topics(request) -> HttpResponse:
    """Show all topics."""
    d_topics = Topic.objects.order_by("date_added")  # ignore pylint: disable=E1101
    context = {"topics": d_topics}
    return render(request, "learning_logs/topics.html", context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    d_topic = Topic.objects.get(id=topic_id)  # ignore pylint: disable=E1101
    entries = d_topic.entry_set.order_by("-date_added")  # type: ignore
    context = {"topic": d_topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)
