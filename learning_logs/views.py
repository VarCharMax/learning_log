"""_summary_

Returns:
    _type_: _description_
"""

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


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


def new_topic(request) -> HttpResponseRedirect | HttpResponse:
    """Add a new topic."""
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topics")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)


def new_entry(request, topic_id) -> HttpResponseRedirect | HttpResponse:
    """Add a new entry for a particular topic."""
    d_topic = Topic.objects.get(id=topic_id)  # ignore pylint: disable=E1101

    if request.method != "POST":
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            f_new_entry = form.save(commit=False)
            f_new_entry.topic = d_topic
            f_new_entry.save()
            return redirect("learning_logs:topic", topic_id=topic_id)

    # Display a blank or invalid form.
    context = {"topic": d_topic, "form": form}
    return render(request, "learning_logs/new_entry.html", context)


def edit_entry(request, entry_id) -> HttpResponseRedirect | HttpResponse:
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)  # ignore pylint: disable=E1101
    d_topic = entry.topic  # type: ignore

    if request.method != "POST":
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topic", topic_id=d_topic.id)  # type: ignore

    # Display a blank or invalid form.
    context = {"entry": entry, "topic": d_topic, "form": form}
    return render(request, "learning_logs/edit_entry.html", context)
