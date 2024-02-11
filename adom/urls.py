from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('#', views.music_view, name='music_view'),
    path('/', views.handle_click, name='handle_click'), 
    path('solfa/', views.handle_click, name='mistake1'),
    path('all/', views.index, name='index'),
    path('all/base.html/', views.base, name='base'),
    path('mhb/', views.handle_click, name='handle_click'),
    path('presby/', views.handle_click_presby, name='handle_click_presby'),
    path('anglican/', views.handle_click_ang, name='handle_click_ang'),
    path('previous/', views.previous_view, name='previous_view'),
    path('search/', views.search_hymn, name='search_hymn'),
    path('search_ang/', views.search_hymn_ang, name='search_hymn_ang'),
    path('search_presby/', views.search_hymn_presby, name='search_hymn_presby'),
    # path('play-music/', views.play_midi, name='play_music'),
    path('download-midi/', views.download_midi, name='download_midi'),
    path('contact/', views.contact, name='contact'),
    path('', views.first, name='first'),
    path('privacy/', views.privacy, name='privacy'), 
    path('anthems/', views.anthems, name='anthems'), 
    path('armah/', views.armah, name='armah'), 
    path('armah_songs/', views.armah_songs, name='armah_songs'), 
    ]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
