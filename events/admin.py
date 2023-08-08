from django.contrib import admin
from events.models import Event, TextPage


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'day', 'month', 'year')


@admin.register(TextPage)
class TextPageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')
