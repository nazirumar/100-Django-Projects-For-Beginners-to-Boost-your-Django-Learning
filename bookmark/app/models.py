from django.db import models

# Create your models here.








_bookmark=(
    ("F", 'favorite'),
    ("P", 'Personal'),
    ("S", 'Social'),
    ("Sp", 'Sport'),
    ("W", 'Weather'),
    ("H", 'Health'),
    ("Wk", 'Work'),
    ("R", 'Research')
)

class BookMark(models.Model):
    category = models.CharField(max_length=300, null=True, blank=True, choices=_bookmark)
    title = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    tags = models.CharField(max_length=200, null=True, blank=True)
    note =models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title