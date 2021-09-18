"""prodigyday URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/

"""
from django.contrib import admin
from django.urls import path
from events import views
from django.conf import settings
from django.conf.urls.static import static
from events.views import AboutView, ContactsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('<int:events_year>/', views.year_list),
    path('<int:event_month>/<int:event_day>/', views.day_detail),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
