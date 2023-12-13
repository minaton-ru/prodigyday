from datetime import date
from django.template import loader
from django.http import HttpResponse
from events.models import Event, TextPage

# Глобальный кортеж с названиями месяцев
month_name_tuple = ('января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                    'июля', 'августа', 'сентября', 'октября', 'ноября',
                    'декабря')


def how_many_years(years_count: int) -> str:
    """
    Функция для определения множественного числа года.
    Принимает число - год.
    Возвращает строку.
    """
    lastDigit = years_count % 10
    if lastDigit == 1:
        return f"{years_count} год назад"
    elif lastDigit in [2, 3, 4] and (years_count < 9 or years_count > 20):
        return f"{years_count} года назад"
    else:
        return f"{years_count} лет назад"


def index(request):
    """Главная страница."""
    # Берем сегодняшнюю дату
    todayDate = date.today()
    template = loader.get_template('index.html')
    # Берем название текущего месяца из кортежа
    this_month_name = month_name_tuple[todayDate.month - 1]
    # Фильтруем события по текущему дню и месяцу формат int
    this_day_list = Event.objects.filter(day=todayDate.day,
                                         month=todayDate.month)
    context = {'this_day_list': this_day_list,
               'this_day': todayDate.day,
               'this_month': this_month_name}
    return HttpResponse(template.render(context))


def year_list(request, events_year):
    """Для страницы всех событий одного года."""
    # Берем сегодняшнюю дату
    todayDate = date.today()
    template = loader.get_template('year_list.html')
    # Фильтруем события по году, который принимает функция
    year_events_list = Event.objects.filter(year=events_year)
    years_count = todayDate.year - events_year
    context = {'year_events_list': year_events_list,
               'how_many_years': how_many_years(years_count),
               # возвращаем в контекст год, который приняла функция
               'events_year': events_year}
    return HttpResponse(template.render(context))


def day_detail(request, event_month, event_day):
    """Для страницы всех событий одного дня."""
    template = loader.get_template('day_detail.html')
    # Берем название нужного месяца из кортежа
    this_month_name = month_name_tuple[event_month - 1]
    # Фильтруем события по дню и месяцу, которые принимает функция
    day_events_list = Event.objects.filter(day=event_day, month=event_month)
    context = {'day_events_list': day_events_list,
               # возвращаем в контекст день, который приняла функция,
               # и название месяца
               'events_day': event_day,
               'events_month': this_month_name}
    return HttpResponse(template.render(context))


def text_page(request, slug):
    """Статичные текстовые страницы."""
    template = loader.get_template('text_page.html')
    page = TextPage.objects.get(slug=slug)
    page_text = page.text
    page_title = page.title
    context = {'page_text': page_text, 'page_title': page_title}
    return HttpResponse(template.render(context))
