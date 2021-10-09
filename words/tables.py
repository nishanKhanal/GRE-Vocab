from table import Table
from table.columns import Column

from .models import Word

class WordTable(Table):
    # id = Column(field='id')
    word = Column(field='word',header="Word", sortable = True, searchable = True)
    meaning = Column(field='meaning', header= "Meaning",sortable = True, searchable = True)
    favourite = Column(field='favourite', header= "Fav",sortable = True, searchable = True)
   
    class Meta:
        model = Word
        search = True
        search_placeholder = u"JPT"
        pagination = True

