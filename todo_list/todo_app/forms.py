from django import forms
from todo_app.models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('user', 'title',)