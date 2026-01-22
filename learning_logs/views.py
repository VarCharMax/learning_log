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
    d_topics = Topic.objects.order_by("date_added")
    context = {"topics": d_topics}
    return render(request, "learning_logs/topics.html", context)
