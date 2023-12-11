from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('solfa/', views.music_view, name='music_view'),
    path('trigger-action/', views.music_view, name='trigger_action'),
    path('all/', views.index, name='index'),
    path('all/base.html/', views.base, name='base'),
    path('', views.handle_click, name='handle_click'),  # Maps /handle-click/ to handle_click view
    path('previous/', views.previous_view, name='previous_view'),
    path('search/', views.search_hymn, name='search_hymn'),
    path('download-midi/', views.download_midi, name='download_midi'),
    path('contact/', views.contact, name='contact'),

]
# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
