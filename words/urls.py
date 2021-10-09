from django.urls import path, include
from .views import WordListView, WordCreateView, WordUpdateView, WordDetailView, WordCardView, WordDeleteView, WordPartialUpdateView, WordTableView

app_name = "words"

urlpatterns = [
    path('', WordCardView.as_view(), name="word_cards"),
    path('list/', WordListView.as_view(), name="word_list"),
    path('table/', WordTableView.as_view(), name="word_table"),
    path('create/', WordCreateView.as_view(), name="word_create"),
    path('update/<int:pk>', WordUpdateView.as_view(), name="word_update"),
    path('partial_update/<int:pk>', WordPartialUpdateView.as_view(), name="word_partial_update"),
    path('detail/<int:pk>', WordDetailView.as_view(), name="word_detail"),
    path('delete/<int:pk>', WordDeleteView.as_view(), name="word_delete"),
]