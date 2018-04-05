from modeltranslation.translator import register, TranslationOptions

from .models import Language


# @register(Language)
class LanguageTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = ('en',)
