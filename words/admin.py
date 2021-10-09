from django.contrib import admin
from .models import Word, Source

from .forms import WordCreateForm

# Register your models here.

class WordAdmin(admin.ModelAdmin):
    # form = WordCreateForm
    autocomplete_fields = ['synonyms', 'antonyms']
    search_fields = ['word']

    list_display = ['word', "_part_of_speech", 'meaning', 'example', '_terms_from_arts_sciences_and_social_sciences','frequent']
    list_display_links = ['word']

    list_filter = ('frequent', 'favourite','difficulty')

    def _part_of_speech(self,obj):
        return obj.part_of_speech
    def _terms_from_arts_sciences_and_social_sciences(self,obj):
        return obj.terms_from_arts_sciences_and_social_sciences

    _terms_from_arts_sciences_and_social_sciences.short_description = "Used Terms"
    _part_of_speech.short_description = "POS"

class SourceAdmin(admin.ModelAdmin):
    model = Source

admin.site.register(Source, SourceAdmin)
admin.site.register(Word, WordAdmin)
