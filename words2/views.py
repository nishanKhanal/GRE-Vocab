from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404

from .models import Word, Meaning
from .forms import WordCreateForm, MeaningCreateForm, MeaningUpdateForm
# Create your views here.

class WordListView(generic.ListView):
    model = Word
    context_object_name = "word_list"
    template_name = "words2/word_list.html"

class WordCardView(generic.ListView):
    model = Word
    context_object_name = "word_list"
    template_name = "words2/word_cards.html"


class WordCreateView(generic.CreateView):
    model = Word
    form_class = WordCreateForm
    template_name = "words2/word_create.html"
    success_url = reverse_lazy('words2:word_cards')

    def get_context_data(self):
        context = super(WordCreateView, self).get_context_data()
        context['action'] = "Add"
        return context

class MeaningCreateView(generic.CreateView):
    model = Meaning
    form_class = MeaningCreateForm
    template_name = "words2/meaning_create.html"
    success_url = reverse_lazy('words2:word_cards')

    def get_context_data(self):
        context = super(MeaningCreateView, self).get_context_data()
        context['action'] = "Add"
        return context

class MeaningUpdateView(generic.UpdateView):
    model = Meaning
    form_class = MeaningUpdateForm
    template_name = "words2/meaning_create.html"
    success_url = reverse_lazy('words2:word_cards')

    def get_context_data(self):
        context = super(MeaningUpdateView, self).get_context_data()
        context['action'] = "Update"
        return context

class WordUpdateView(generic.UpdateView):
    model = Word
    form_class = WordCreateForm
    template_name = "words2/word_create.html"
    success_url = reverse_lazy('words2:word_cards')

    def get_context_data(self,**kwargs):
        context = super(WordUpdateView, self).get_context_data()
        context['action'] = "Update"
        return context

class WordUpdateDifficultyView(generic.View):
    def post(self, request, pk):
        word = get_object_or_404(Word,id=pk)
        word.difficulty = request.POST.get('difficulty')
        word.save();
        return redirect(reverse_lazy('words2:word_cards'))

class WordDetailView(generic.DetailView):
    model = Word
    template_name = "words2/word_detail.html"
    context_object_name = "word"

class WordDeleteView(generic.DeleteView):
    model = Word
    success_url = reverse_lazy("words2:word_cards")


# def list(request):
#     return render(request, "words/list.html", context={})
