from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class ModelWithTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Word(ModelWithTimeStamp):
    word = models.CharField(max_length=100)
    difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=1)
    favourite = models.BooleanField(default=False, blank=True)
    translation = models.CharField(max_length=255, blank=True)
    audio_link = models.URLField(blank=True)

    class Meta:
        ordering = ('-updated_at',)

    def __str__(self):
        return self.word

    def get_absolute_url(self):
        return reverse("words2:word_detail", kwargs={"pk": self.pk})

class Meaning(ModelWithTimeStamp):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name="meanings")
    part_of_speech = models.CharField(max_length=50);
    definition = models.TextField(blank=True)
    synonyms = models.ManyToManyField(Word, related_name="synonyms", blank=True)
    antonyms = models.ManyToManyField(Word, related_name="antomyms", blank=True)
    example = models.TextField(blank=True)
    translation = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.definition

    
    def get_absolute_url(self):
        return reverse("words2:word_detail", kwargs={"pk": self.word.pk})




