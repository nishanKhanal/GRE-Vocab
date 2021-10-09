from django.contrib import admin
from .models import Word, Meaning
# Register your models here.

class MeaningInlines(admin.TabularInline):
    autocomplete_fields = ['synonyms', 'antonyms']
    model = Meaning
    extra = 1

class Word2Admin(admin.ModelAdmin):
    inlines = [MeaningInlines]
    search_fields = ['word']
    model = Word

admin.site.register(Word, Word2Admin)