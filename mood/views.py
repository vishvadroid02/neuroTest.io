from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Mood
from .serializers import MoodSerializer

from datetime import date

from datetime import timedelta
# Create your views here.

#creating an API to 'GET', 'POST' methods
@api_view(['GET', 'POST'])
def mood(request):
    if request.method == 'GET':
        streak = 0
        if request.user.is_authenticated:
            today = date.today()
            three_days_ago = date.today() + timedelta(days=-3)
            username = request.user.username

            mood = Mood.objects.filter(streak_user=username)
            streak = Mood.objects.filter(streak_user=username, streak_date__lt=today, streak_date__gt=three_days_ago).count()
            
            print(streak)
                
        else:
            mood = Mood.objects.all()

        serializer = MoodSerializer(mood, many=True)
        
        data = serializer.data
        data.update({'streak':streak})
        return Response(data)

    elif request.method == 'POST':
        serializer = MoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    #error handling. bad request !!!        
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                



