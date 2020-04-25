from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from flashcards.models import WordAssociation, WordAssociationSet


class WordAssociationList(ListView):
    """
    View for word associations
    """
    model = WordAssociation


class WordAssociationSetList(ListView):
    """
    View for sets of word associations
    """
    model = WordAssociationSet
