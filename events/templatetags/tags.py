"""
Файл для кастомных тегов.
В шаблонах подключается по имени файла с помощью {% load tags %}
"""

from django import template
from events.models import Event, TextPage

register = template.Library()

@register.inclusion_tag('tags/all_years_list.html')
def show_all_years(): # создаем кастомный тег для списка всех годов, чтобы использовать в html-шаблонах
    all_years_list = set(Event.objects.values_list('year', flat=True)) # все значения поля year (не кортежи), множество убирает дубли
    all_years_count = {}
    for year in sorted(all_years_list):
        all_years_count[year] = Event.objects.filter(year=year).count() # наполняем словарь, ключ - год, значение - количество записей по этому году
    return { 'all_years_list': all_years_count } # возвращаем словарь

@register.inclusion_tag('tags/text_pages_list.html')
def show_all_text_pages(): # создаем кастомный тег для списка всех статичных текстовых страниц, чтобы использовать в html-шаблонах
    all_text_pages_list = TextPage.objects.all()
    return { 'all_text_pages_list': all_text_pages_list }