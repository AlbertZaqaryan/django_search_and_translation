from .models import Nout
from modeltranslation.translator import register, TranslationOptions

@register(Nout)
class NoutTranslationOptions(TranslationOptions):
    fields = ('name', 'about',)