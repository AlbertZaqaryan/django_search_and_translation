from django.db import models

# Create your models here.

class Nout(models.Model):

    name = models.CharField('Nout name', max_length=60)
    price = models.PositiveBigIntegerField('Nout price')
    img = models.ImageField('Nout image', upload_to='images')
    about = models.TextField('Nout about')
    check_nout = models.BooleanField('Nout check Yes/No')
    slug = models.SlugField('Nout slug', unique=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Nout'
        verbose_name_plural = 'Nouts'
        ordering = ['price']