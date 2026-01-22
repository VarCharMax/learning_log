"""_summary_"""

from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Form for creating and updating Topic instances."""

    class Meta:  # ignore pylint: disable=too-few-public-methods
        """Provide metadata about the form."""

        model = Topic
        fields = ["text"]
        labels = {"text": ""}


class EntryForm(forms.ModelForm):
    """Form for creating and updating Entry instances."""

    class Meta:  # ignore pylint: disable=too-few-public-methods
        """Provide metadata about the form."""

        model = Entry
        fields = ["text"]
        labels = {"text": "Entry:"}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
