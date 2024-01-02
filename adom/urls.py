from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('#', views.music_view, name='music_view'),
    path('solfa/', views.handle_click, name='mistake1'),
    path('all/', views.index, name='index'),
    path('all/base.html/', views.base, name='base'),
    path('mhb/', views.handle_click, name='handle_click'),  # Maps /handle-click/ to handle_click view
    path('anglican/', views.handle_click_ang, name='handle_click_ang'),
    path('previous/', views.previous_view, name='previous_view'),
    path('search/', views.search_hymn, name='search_hymn'),
    path('search_ang/', views.search_hymn_ang, name='search_hymn_ang'),
    # path('play-music/', views.play_midi, name='play_music'),
    path('download-midi/', views.download_midi, name='download_midi'),
    path('contact/', views.contact, name='contact'),
    path('', views.first, name='first'),


]
# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
