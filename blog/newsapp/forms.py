from newsapp.models import Blog
from django import forms
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):
    desc = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Blog
        fields = '__all__'