from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your models here.

class ModelWithTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Source(ModelWithTimeStamp):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Word(ModelWithTimeStamp):
    word = models.CharField(max_length=100)
    part_of_speech = models.CharField(max_length=25,)
    meaning = models.TextField(blank=True)
    favourite = models.BooleanField(blank=True, default=False)
    frequent = models.BooleanField(blank=True, default=False)
    unit = models.IntegerField(blank=True,null=True,default=None)
    synonyms = models.ManyToManyField('self', related_name="synonyms", blank=True)
    antonyms = models.ManyToManyField('self', related_name="antomyms", blank=True)
    example = models.TextField(blank=True)
    terms_from_arts_sciences_and_social_sciences = models.TextField(blank=True, null=True, default=None)
    source = models.ForeignKey(Source, related_name="words", on_delete=models.DO_NOTHING,blank=True,null=True)
    word_translation = models.CharField(max_length=250,blank=True)
    meaning_translation = models.CharField(max_length=250,blank=True)
    difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=1)
    last_read_at = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None,blank=True, null=True)


    def save(self,*args, **kwargs):
        try:
            this = Word.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except: pass

        # Opening the uploaded image
        try:
            im = Image.open(self.image)
            im = im.convert('RGB')
            output = BytesIO()

            # after modifications, save it to the output
            im.save(output, format='JPEG', quality=10)
            output.seek(0)
            

            # change the imagefield value to be the newley modifed image value
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'images/jpeg',
                                            sys.getsizeof(output), None)
        except Exception as e:
            print(e)
        super(Word, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('-last_read_at','word','-difficulty','-updated_at',)

    def __str__(self):
        return self.word

    def get_absolute_url(self):
        return reverse("words:word_detail", kwargs={"pk": self.pk})


