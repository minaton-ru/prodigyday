from django.contrib import admin
from django.urls import path
from events import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('<int:events_year>/', views.year_list),
    path('<int:event_month>/<int:event_day>/',
         views.day_detail, name='day_detail'),
    path('<slug>/', views.text_page, name='text_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
