from django.test import TestCase
from events.models import Event, TextPage


class EventModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Event.objects.create(title='The single Ibiza',
                             content='The single Ibiza was released.',
                             day=23, month=3, year=2015)

    def test_event_title_max_length(self):
        """The maximun length of the title field is 100."""
        event = Event.objects.get(id=1)
        self.assertIsInstance(event, Event)
        max_length = event._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_event_content_max_length(self):
        """The maximun length of the content field is 1000."""
        event = Event.objects.get(id=1)
        self.assertIsInstance(event, Event)
        max_length = event._meta.get_field('content').max_length
        self.assertEquals(max_length, 1000)

    def test_object_name_is_title(self):
        """Str() of the object is its title."""
        event = Event.objects.get(id=1)
        self.assertIsInstance(event, Event)
        expected_object_name = event.title
        self.assertEquals(expected_object_name, str(event))

    def test_get_absolute_url(self):
        """The canonical URL for the object is its month and day by slashes."""
        event = Event.objects.get(id=1)
        self.assertIsInstance(event, Event)
        self.assertEquals(event.get_absolute_url(),
                          f'/{event.month}/{event.day}/')


class TextPageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        TextPage.objects.create(slug='newpage',
                                title='New text page',
                                text='This new text page was created for test.')

    def test_text_page_title_max_length(self):
        """The maximun length of the title field is 100."""
        page = TextPage.objects.get(id=1)
        self.assertIsInstance(page, TextPage)
        max_length = page._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_text_page_text_max_length(self):
        """The maximun length of the text field is 2000."""
        page = TextPage.objects.get(id=1)
        self.assertIsInstance(page, TextPage)
        max_length = page._meta.get_field('text').max_length
        self.assertEquals(max_length, 2000)

    def test_object_name_is_title(self):
        """Str() of the object is its title."""
        page = TextPage.objects.get(id=1)
        self.assertIsInstance(page, TextPage)
        expected_object_name = page.title
        self.assertEquals(expected_object_name, str(page))

    def test_get_absolute_url(self):
        """The canonical URL for the object is its slug."""
        page = TextPage.objects.get(id=1)
        self.assertIsInstance(page, TextPage)
        self.assertEquals(page.get_absolute_url(), '/newpage/')
