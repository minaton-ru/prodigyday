"""
Файл для кастомных тегов.
В шаблонах подключается по имени файла с помощью {% load tags %}
"""
from collections import Counter
from django import template
from events.models import Event, TextPage

register = template.Library()


# создаем кастомный тег для списка всех годов,
# чтобы использовать в html-шаблонах
@register.inclusion_tag('tags/all_years_list.html')
def show_all_years():
    # все значения поля year (не кортежи)
    all_years_list = Event.objects.values_list('year',
                                               flat=True).order_by('year')
    # Из объекта Counter создаем словарь
    # ключ - год, значение - количество записей по этому году
    all_years_count = dict(Counter(all_years_list))
    return {'all_years_list': all_years_count}


# создаем кастомный тег для списка всех статичных текстовых страниц,
# чтобы использовать в html-шаблонах
@register.inclusion_tag('tags/text_pages_list.html')
def show_all_text_pages():
    all_text_pages_list = TextPage.objects.all()
    return {'all_text_pages_list': all_text_pages_list}
