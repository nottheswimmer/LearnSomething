from django.db import models


# Create your models here.
class WordAssociationSet(models.Model):
    """
    A set of word asociations
    """
    name = models.CharField(max_length=255, help_text='The name of this set of word associations')

    def __str__(self):
        return f"WordAssociationSet({self.name=})"


class WordAssociation(models.Model):
    """
    Pairs a word in a language you know with a word in a language you don't
    """
    word_set = models.ManyToManyField('WordAssociationSet', help_text='The set of words this word appears in')

    # Longest word in English is 45 characters. 255 seems like a sensible maximum.
    known_word = models.CharField(max_length=255, help_text="A word in a language you know")
    learning_word = models.CharField(max_length=255, help_text="The word in the language you're learning")

    class Meta:
        unique_together = [
            ['known_word', 'learning_word'],
        ]

    def __str__(self):
        return f'WordAssociation({self.known_word=}, {self.learning_word=})'

    def clean_known_word(self):
        """
        Make sure known words are stripped and lowercase
        """
        known_word = self.cleaned_data['known_word']
        known_word = known_word.lower().strip()
        return known_word

    def clean_learning_word(self):
        """
        Make sure learning words are stripped and lowercase
        """
        learning_word = self.cleaned_data['learning_word']
        learning_word = learning_word.lower().strip()
        return learning_word
