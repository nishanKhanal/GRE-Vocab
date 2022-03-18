from django import forms
from .models import Word, Source

from django_select2 import forms as s2forms

class SynonymsWidget(s2forms.Select2MultipleWidget):
    search_fields = [
        "word__icontains",
        # "meaning__icontains",
    ]
    model = Word
    def build_attrs(self, base_attrs, extra_attrs=None):
        attrs = super().build_attrs(base_attrs, extra_attrs=extra_attrs)
        if "class" in attrs:
            attrs["class"] += " select-dark"
        return attrs

    queryset = Word.objects.all()



class WordCreateForm(forms.ModelForm):
    words_choices = Word.objects.all()
    style_attributes = {'style': "background: #121212; color: rgba(255,255,255,0.87); margin-bottom: 15px;"}

    word = forms.CharField(label="Word",max_length=100, widget=forms.TextInput(attrs=style_attributes))
    meaning = forms.CharField(label="Meaning",widget=forms.Textarea(attrs=style_attributes),required=False)
    part_of_speech = forms.CharField(label="Part Of Speech",widget=forms.TextInput(attrs=style_attributes),required=False)
    # synonyms = forms.ModelMultipleChoiceField(label="Synonyms",required=False, queryset=words_choices)
    # antonyms = forms.ModelMultipleChoiceField(label="Antonyms",required=False, queryset=words_choices)
    example = forms.CharField(label="Example", widget=forms.Textarea(attrs=style_attributes),required=False)
    terms_from_arts_sciences_and_social_sciences = forms.CharField(label="Used Terms", widget=forms.Textarea(attrs=style_attributes),required=False)
    word_translation = forms.CharField(label="Word Translation",max_length=250, widget=forms.TextInput(attrs=style_attributes),required=False)
    meaning_translation = forms.CharField(label="Meaning Translation",max_length=250, widget=forms.TextInput(attrs=style_attributes),required=False)
    hint = forms.CharField(label="Hint", widget=forms.TextInput(attrs=style_attributes),required=False)
    difficulty = forms.IntegerField(label="Difficulty", widget=forms.NumberInput(attrs=style_attributes),required=True)

    class Meta:
        style_attributes = {'style': "background-color: black; text-color: black; margin-bottom: 30px;"}

        model = Word
        exclude =  ('frequent','last_read_at','favourite','unit')
        widgets = {
            "synonyms": SynonymsWidget,
            "antonyms": s2forms.Select2MultipleWidget(attrs={'class' : 'bg-dark text-white'}),
            "sources": s2forms.Select2MultipleWidget(attrs={'class' : 'bg-dark text-white'}),
        }

    def __init__(self, *args, **kwargs):
        super(WordCreateForm, self).__init__(*args, **kwargs)
        # self.fields['synonyms'].widget.attrs.update({
        #     'style': 'background: black; color: black;'
        # })
        self.fields['difficulty'].initial = 1
