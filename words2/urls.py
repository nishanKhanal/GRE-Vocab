from django.urls import path, include
from .views import WordListView, WordCreateView, WordUpdateView, WordDetailView, WordCardView, WordDeleteView, WordUpdateDifficultyView, MeaningCreateView, MeaningUpdateView

app_name = "words2"

urlpatterns = [
    path('', WordCardView.as_view(), name="word_cards"),
    path('list/', WordListView.as_view(), name="word_list"),
    path('create/', WordCreateView.as_view(), name="word_create"),
    path('update/<int:pk>', WordUpdateView.as_view(), name="word_update"),
    path('update_difficulty/<int:pk>', WordUpdateDifficultyView.as_view(), name="word_update_difficulty"),
    path('detail/<int:pk>', WordDetailView.as_view(), name="word_detail"),
    path('delete/<int:pk>', WordDeleteView.as_view(), name="word_delete"),

    path('meaning/create/', MeaningCreateView.as_view(), name="meaning_create"),
    path('meaning/update/<int:pk>', MeaningUpdateView.as_view(), name="meaning_create"),

]