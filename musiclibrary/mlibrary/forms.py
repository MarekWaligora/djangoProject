from django import forms
from django.forms import SelectMultiple

from .models import MusicKind,Artist,Album,Borrower,Borrow


class AddArtistForm(forms.Form):
    """ add artrist to the list """

