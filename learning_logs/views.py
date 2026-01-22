"""_summary_

Returns:
    _type_: _description_
"""

from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    """The home page for Learning Log."""
    return render(request, "learning_logs/index.html")
