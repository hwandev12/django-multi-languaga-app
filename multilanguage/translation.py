from modeltranslation.translator import register, TranslationOptions
from .models import Details

@register(Details)
class DetailsTranslationOptions(TranslationOptions):
    fields = ('name', 'text',)