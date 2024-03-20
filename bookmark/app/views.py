from django.shortcuts import redirect, render
from django.db.models import Count

from app.forms import BookmarkForm
from app.models import BookMark

# Create your views here.


def bookmark(request):
    categories = set([choice[0] for choice in BookMark._meta.get_field('category').choices])
        
    # Create a dictionary to hold bookmarks grouped by category
    bookmarks_by_category = {}

    for category in categories:
        # Filter bookmarks for the current category
        bookmarks = BookMark.objects.filter(category=category)
        
        # Add bookmarks to the dictionary
        bookmarks_by_category[category] = bookmarks

    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={
        'form':BookmarkForm(),
        'bookmarks_by_category': bookmarks_by_category

    }
    return render(request, 'index.html', context)