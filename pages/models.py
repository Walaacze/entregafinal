from django.db import models
from ckeditor.fields import RichTextField
from datetime import date

# Create your models here.

class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    fecha = models.DateField(default = date.today)
    cuerpo = RichTextField(null = True, blank = True)
    # imagen = models.ImageField(upload_to= 'imagen/', null = True, blank = True)
    
    
    def __str__(self):
        return f'{self.titulo}'
