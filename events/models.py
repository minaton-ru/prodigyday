from django.db import models

class Event(models.Model):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12
    MONTH_CHOICES = [
        (JANUARY, 'января'),
        (FEBRUARY, 'февраля'),
        (MARCH, 'марта'),
        (APRIL, 'апреля'),
        (MAY, 'мая'),
        (JUNE, 'июня'),
        (JULY, 'июля'),
        (AUGUST, 'августа'),
        (SEPTEMBER, 'сентября'),
        (OCTOBER, 'октября'),
        (NOVEMBER, 'ноября'),
        (DECEMBER, 'декабря'),
    ]
    title = models.CharField(max_length=255)
    content = models.TextField()
    day = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField(choices=MONTH_CHOICES)
    year = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='pics', null=True, blank=True)

    def __str__(self):
	    return self.title
