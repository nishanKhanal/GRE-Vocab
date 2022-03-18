import django_filters

from django import forms

from django_select2 import forms as s2forms
from django_filters import RangeFilter, AllValuesFilter, CharFilter
from .models import Word, Source

difficulty_choices = [(i,i) for i in range(1,11)]
unit_choices = [(i,i) for i in range(1,81)]
dark_background_attrs = {'class' : 'bg-dark text-white'}

class WordFilter(django_filters.FilterSet):
    # word = CharFilter(field_name="word", lookup_expr='icontains')
    # part_of_speech = CharFilter(field_name="part_of_speech", lookup_expr='icontains')
    # meaning = CharFilter(field_name="meaning", lookup_expr='icontains')
    
    sources = django_filters.ModelMultipleChoiceFilter(label="Sources:",queryset=Source.objects.all(), widget=forms.CheckboxSelectMultiple,)
    # difficulty = django_filters.NumberFilter(widget=s2forms.Select2Widget(attrs=dark_background_attrs,choices=difficulty_choices))
    frequent = django_filters.BooleanFilter(widget=forms.RadioSelect(choices=[(None,"ALL"),(True,"yes"),(False,"No")]))
    favourite = django_filters.BooleanFilter(widget=forms.RadioSelect(choices=[(None,"ALL"),(True,"yes"),(False,"No")]))
    difficulty = django_filters.NumberFilter(field_name="difficulty",lookup_expr="gt",widget=forms.NumberInput(attrs=dark_background_attrs))
    unit = django_filters.NumberFilter(field_name="unit",widget=forms.NumberInput(attrs=dark_background_attrs))
    word_starts_with = CharFilter(field_name="word", lookup_expr='istartswith',widget=forms.TextInput(attrs=dark_background_attrs))
    word = CharFilter(field_name="word", lookup_expr='icontains',widget=forms.TextInput(attrs=dark_background_attrs))


    class Meta:
        model = Word
        # fields = {
        #     'word': ['icontains'],
        #     # 'difficulty' : ['lt','gt']
        #     }
        fields= []


# class AllRangeFilter(RangeFilter):
#     def __init__ (self, *args, **kwargs):
#         super(). __init__ (*args, **kwargs)
#         min_value = 1
#         max_value = 10
#         self.extra['widget'] = CustomRangeWidget(attrs={'data-range_min':min_value,'data-range_max':max_value})
