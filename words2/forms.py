from django import forms
from .models import Word, Meaning

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

class WordsWidget(s2forms.Select2Widget):
    search_fields = [
        "word__icontains",
        # "meaning__icontains",
    ]
    model = Word
    # def build_attrs(self, base_attrs, extra_attrs=None):
    #     attrs = super().build_attrs(base_attrs, extra_attrs=extra_attrs)
    #     if "class" in attrs:
    #         attrs["class"] += " select-dark"
    #     return attrs

    queryset = Word.objects.all()



class WordCreateForm(forms.ModelForm):
    style_attributes = {'style': "background: #121212; color: rgba(255,255,255,0.87); margin-bottom: 15px;"}
    word = forms.CharField(label="Word", widget=forms.TextInput(attrs=style_attributes))
    difficulty = forms.IntegerField(label="Difficulty", widget=forms.TextInput(attrs=style_attributes), required=True)

    class Meta:
        style_attributes = {'style': "background-color: black; text-color: black; margin-bottom: 30px;"}

        model = Word
        exclude = ('favourite','translation', 'audio_url')

    def save(self, commit=True):
        word = super(WordCreateForm, self).save(commit=False)
        

        if commit:
            word.save()
        return m

    def __init__(self, *args, **kwargs):
        super(WordCreateForm, self).__init__(*args, **kwargs)
        self.fields['difficulty'].initial=1

    




class MeaningCreateForm(forms.ModelForm):
    words_choices = Word.objects.all()
    style_attributes = {'style': "background: #121212; color: rgba(255,255,255,0.87); margin-bottom: 15px;"}

    # word = forms.(label="Word",max_length=100, widget=forms.TextInput(attrs=style_attributes))
    definition = forms.CharField(label="Meaning",widget=forms.Textarea(attrs=style_attributes),required=False)
    # synonyms = forms.ModelMultipleChoiceField(label="Synonyms",required=False, queryset=words_choices)
    # antonyms = forms.ModelMultipleChoiceField(label="Antonyms",required=False, queryset=words_choices)
    example = forms.CharField(label="Example", widget=forms.Textarea(attrs=style_attributes),required=False)
    translation = forms.CharField(label="Translation",max_length=250, widget=forms.TextInput(attrs=style_attributes),required=False)
    difficulty = forms.IntegerField(label="Difficulty", widget=forms.TextInput(attrs=style_attributes), required=True)

    class Meta:
        style_attributes = {'style': "background-color: black; text-color: black; margin-bottom: 30px;"}

        model = Meaning
        fields = '__all__'
        widgets = {
            "word": WordsWidget,
            "synonyms": SynonymsWidget,
            "antonyms": s2forms.Select2MultipleWidget(attrs={'class' : 'bg-dark text-white'}),
        }
class MeaningUpdateForm(MeaningCreateForm):
    word = forms.ModelChoiceField(label="Word",widget=WordsWidget,disabled=False, queryset=Word.objects.all())
