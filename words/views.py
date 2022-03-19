from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

import requests, json

from .models import Word
from .forms import WordCreateForm
from .tables import WordTable
from .services.translate import translate

from .filters import WordFilter
# Create your views here.

class WordListView(generic.ListView):
    model = Word
    context_object_name = "word_list"
    template_name = "words/word_list.html"

class WordCardView(generic.ListView):
    model = Word
    context_object_name = "word_list"
    template_name = "words/word_cards.html"
    paginate_by = 20



    def get_context_data(self, **kwargs):
        context = super(WordCardView, self).get_context_data()
        wordFilter = WordFilter(self.request.GET, self.get_queryset())   
        context['query_string'] = self.request.GET
        context['wordFilter'] = wordFilter
        return context

    def get_queryset(self):
        object_list = self.model.objects.all()
        search_term = self.request.GET.get('search_term', '')
        sort_by = self.request.GET.get('sort_by', '')
        sort_order = self.request.GET.get('sort_order', '')
        if sort_by:
            if sort_order == "reverse":
                sort_by = "-"+sort_by
            object_list = object_list.order_by(sort_by)
        if search_term:
            object_list = object_list.filter(Q(word__icontains=search_term)| Q(meaning__icontains=search_term))

        wordFilter = WordFilter(self.request.GET,object_list)
        return wordFilter.qs

class WordCardViewExtra(WordCardView):
    def get_queryset(self):
        object_list = self.model.objects.exclude(sources__name__icontains = "Barron")
        return object_list


class WordCreateView(LoginRequiredMixin,generic.CreateView):
    model = Word
    form_class = WordCreateForm
    login_url = reverse_lazy("login")
    template_name = "words/word_create.html"
    success_url = reverse_lazy('words:word_cards')

    def get_context_data(self, **kwargs):
        context = super(WordCreateView, self).get_context_data()
        context['action'] = "Add"
        return context

class WordUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Word
    form_class = WordCreateForm
    login_url = reverse_lazy("login")
    template_name = "words/word_create.html"
    success_url = reverse_lazy('words:word_cards')

    def get_context_data(self,**kwargs):
        context = super(WordUpdateView, self).get_context_data()
        context['action'] = "Update"
        return context

class WordPartialUpdateView(LoginRequiredMixin,generic.View):
    login_url = reverse_lazy("login")

    def get(self,request, pk):
        return HttpResponseRedirect("/")

    def post(self, request, pk):
        word = get_object_or_404(Word,id=pk)
        word.difficulty = request.POST.get('difficulty',word.difficulty)
        word.favourite = bool(request.POST.get('favourite',word.favourite))
        word.last_read_at = timezone.now() if 'last_read_at' in request.POST else word.last_read_at
        if 'translate' in request.POST:
           translate(word)

        word.save();
        next = request.POST.get('next','')
        return HttpResponseRedirect(next)

class WordDetailView(generic.DetailView):
    model = Word
    template_name = "words/word_detail.html"
    context_object_name = "word"

class WordDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy("login")
    model = Word
    success_url = reverse_lazy("words:word_cards")

class WordTableView(generic.View):
    def get(self, request):
        wordTable = WordTable()
        return render(request, "words/word_table.html", {'wordTable': wordTable})

# def list(request):
#     return render(request, "words/list.html", context={})
