"""
Файл для кастомных тегов.
В шаблонах подключается по имени файла с помощью {% load tags %}
"""

from django import template
from events.models import Event, TextPage

register = template.Library()

@register.inclusion_tag('all_years_list.html')
def show_all_years(): # создаем кастомный тег для списка всех годов, чтобы использовать в html-шаблонах
    all_years_list = Event.objects.values_list('year', flat=True).distinct() # берем значения поля year, возвращаем список значений, а не кортежей, убираем дубли
    return { 'all_years_list': sorted(all_years_list) }

@register.inclusion_tag('text_pages_list.html')
def show_all_text_pages(): # создаем кастомный тег для списка всех статичных текстовых страниц, чтобы использовать в html-шаблонах
    all_text_pages_list = TextPage.objects.all()
    return { 'all_text_pages_list': all_text_pages_list }