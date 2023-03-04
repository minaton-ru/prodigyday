from django.contrib import admin
from django.urls import path
from events import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('<int:events_year>/', views.year_list),
    path('<int:event_month>/<int:event_day>/', views.day_detail),
    path('about/', views.about_page, name='about'),
    path('contacts/', views.contacts_page, name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
