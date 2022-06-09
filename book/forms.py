from django import froms
from . import models

class BookForm(froms.ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"
