from django import forms

from app.models import BookMark


class BookmarkForm(forms.ModelForm):
    """Form definition for Bookmark."""

    class Meta:
        """Meta definition for Bookmarkform."""

        model = BookMark
        fields = '__all__'
