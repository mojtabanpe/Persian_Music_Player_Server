from django.urls import path

from player import views

urlpatterns = [
    path('upload', views.Upload.as_view()),
    path('musics', views.MusicsList.as_view()),
    path('music_one/<int:pk>', views.MusicDetail.as_view()),
]