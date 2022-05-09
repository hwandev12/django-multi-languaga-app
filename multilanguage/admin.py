from django.contrib import admin
from .models import Details
from modeltranslation.admin import TranslationAdmin

@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}