from django.db import models
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from .models import *
from .serializers import MusicSerializer
import os


class Upload(APIView):
    def post(self, request, *args, **kwargs):
        siteUrl = 'http://130.185.78.154:8001/'
        # siteUrl = 'http://localhost:8000/'
        try:          
            file = request.FILES['myFile']
            name = str(file.name).split('.')[0].replace(' ', '').replace('_', '')
            try:
                destination = open(f'../files/musics/{name}.mp3', 'wb+')
            except Exception as e1:
                path = './files/musics'
                try:
                    os.mkdir(path)
                except Exception as e:
                    return Response(path,status=status.HTTP_400_BAD_REQUEST)
                destination = open(f'../files/musics/{name}.mp3', 'wb+')
            for chunk in file.chunks():
                destination.write(chunk)
            destination.close()
            message = destination.name;
            message = message.replace('../',siteUrl)
            message = message.replace('./',siteUrl)
            # message = message.replace('./',os.path.join(BASE_DIR, ''))
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:       
                return Response(e,status=status.HTTP_400_BAD_REQUEST)

class MusicsList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer