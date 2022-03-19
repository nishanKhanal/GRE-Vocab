from django.core.management.base import BaseCommand, CommandError
from words.models import Word, Source
import re


class Command(BaseCommand):
    help = "seed database with words"

    def add_arguments(self, parser):
        parser.add_argument("-l","--limit", type=int , default=101, help="Number of Words to be inserted")
        parser.add_argument("-s","--source", type=str , help="Number of Words to be inserted")
        parser.add_argument("-d","--delete_all", action="store_true", help="Delete All words from Barron")

    def handle(self, *args, **options):
        
        if options['limit'] < 0:
            raise CommandError("Limit must be positive")
        
        if not options['source']:
            raise CommandError("Source must not be empty")
        if options['source'].lower() == "barron":
            
            if options['delete_all']:
                Word.objects.filter(sources__name = "Barron").delete()
                return

            with open('words/resources/barron_text_book.txt','r') as barron_text_book:
                string = barron_text_book.read()

            matches = re.findall(r"(\*?[a-zA-Z]*)\s([avdjn]{1,3}\.)\s(.*?)(?=\*?[a-zA-Z]*\s[avdjn]{1,3}\.)", string.strip(),flags=re.DOTALL)[:options['limit']]

            for i in range(len(matches)):
                matches[i] = list(matches[i])

            regex_search_term_REVIEW = r"REVIEW.*UNIT\s(\d)*"
            regex_search_term_ESSENTIAL = r"\d*\s*ESSENTIAL WORDS FOR THE GRE"
            regex_replacement_BLANK = ""
            unit = 1
            for match in matches:
                match[1] += str(unit)
                if '*' in match[0]:
                    match[0] = match[0][1:]+"*"
                if "bored because of frequent indulgence; unconcerned" in match[2]:
                    match[0] = "blase"
                if "REVIEW" in match[2]:
                    unit += 1
                    match[2] = re.sub(regex_search_term_REVIEW, regex_replacement_BLANK, match[2],flags=re.DOTALL)
                if "ESSENTIAL WORDS FOR THE GRE" in match[2]:
                    match[2] = re.sub(regex_search_term_ESSENTIAL, regex_replacement_BLANK, match[2],flags=re.DOTALL)
                
                match[2] = match[2].replace("-\n","")
                pattern = re.match(r"(.*?)(?=\n\“?[A-Z])", match[2], flags=re.DOTALL)
                if pattern is not None:
                    definition = match[2][:pattern.end()]
                    examples = match[2][pattern.end()+1:]
                    match[2] = definition
                    match += [examples]
                    
                
                terms_pattern = re.match(r"(.*)(\nTerms from the Arts, Sciences, and Social Sciences)",match[3],flags=re.DOTALL)    
                if terms_pattern is not None:
                    terms = match[3][terms_pattern.end()+1:]
                    match[3] = terms_pattern.groups()[0]
                    match += [terms]
                    
                match[3] = match[3].replace("\n"," ")
                match[3] = re.sub(r"([a-zA-Z]{2,}[.\"\”\?])(\s)([A-Z])",r"\1\n\3",match[3])
                
                
                try:
                    match[4] = re.sub(r"\n([\w]*\s?[\w]*:)",r"\r\1",match[4],flags=re.DOTALL)
                    match[4] = match[4].replace("\n"," ").replace("\r","\n")
                except:
                    pass


            barron, created = Source.objects.get_or_create(name="Barron")
            for match in matches:
                try:
                    try: 
                        used_terms = match[4]
                    except:
                        used_terms = None
                    word = Word.objects.create(word=match[0].lower(),part_of_speech=match[1][:match[1].index('.')+1], meaning= match[2], example=match[3],frequent= True if '*' in match[0] else False,terms_from_arts_sciences_and_social_sciences = used_terms, unit = int(match[1][match[1].index('.')+1:]))
                    word.sources.add(barron)
                except Exception as e:
                    print(e)
                    print(match)
            return

        if options['source'].lower() == "101frequentwords":
            if options['delete_all']:
                Word.objects.filter(sources__name = "101 Frequent Words").delete()
                return
            from bs4 import BeautifulSoup

            with open("words/resources/101_frequent_words.xml") as xmlfile:
                soup = BeautifulSoup(xmlfile, 'html.parser')
                frequentWords101, created = Source.objects.get_or_create(name="101 Frequent Words")
                
                for data in soup.findAll('data'):
                    word = Word.objects.create(word=data.word.text.lower(),part_of_speech=data.pos.text.lower(), meaning=data.meaning.text.lower(),example=data.example.text.lower())
                    word.sources.add(frequentWords101)
            return
        else:
            raise CommandError("Please enter a valid Source")

