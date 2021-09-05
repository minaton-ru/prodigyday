from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from datetime import date # импортируем модуль для работы с датой
from events.models import Event

todayDate = date.today() # берем сегодняшнюю дату глобально
month_name_tuple = ('января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря') # глобальный кортеж с названиями месяцев

def index(request): # главная страница
    template = loader.get_template('index.html')
    this_month_name = month_name_tuple[todayDate.month - 1] # берем название текущего месяца из кортежа
    this_day_list = Event.objects.filter(day=todayDate.day, month=todayDate.month) # фильтруем события по текущему дню и месяцу формат int
    context = { 'this_day_list': this_day_list,
    'this_day': todayDate.day,
    'this_month': this_month_name, }
    return HttpResponse(template.render(context))

def year_list(request, events_year): # для страницы всех событий одного года
    template = loader.get_template('year_list.html')
    year_events_list = Event.objects.filter(year=events_year) # фильтруем события по году, который принимает функция
    context = { 'year_events_list': year_events_list,
    'events_year': events_year} # возвращаем в контекст год, который приняла функция
    return HttpResponse(template.render(context))

def day_detail(request, event_month, event_day): # для страницы всех событий одного дня
    template = loader.get_template('day_detail.html')
    this_month_name = month_name_tuple[event_month - 1] # берем название нужного месяца из кортежа
    day_events_list = Event.objects.filter(day=event_day, month=event_month) # фильтруем события по дню и месяцу, которые принимает функция
    context = { 'day_events_list': day_events_list,
    'events_day': event_day, # возвращаем в контекст день, который приняла функция, и название месяца
    'events_month': this_month_name }
    return HttpResponse(template.render(context))