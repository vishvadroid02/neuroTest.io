from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count

from .models import Mood, Streak
from .serializers import MoodSerializer
from datetime import date
from datetime import timedelta
import json
# Create your views here.


@api_view(['GET', 'POST'])
def mood(request):
    today = date.today()
    print(today)
    if request.user.is_authenticated:
        username = request.user.username
        user_streak = Streak.objects.filter(streak_user=username)
    else:
        user_streak = False

    if request.method == 'GET':
        streak = 0
        percentile = 0

        if request.user.is_authenticated:
            username = request.user.username

            mood = Mood.objects.filter(streak_user=username)

            if user_streak:
                streak = user_streak[0].streak_count    
                highest = Streak.objects.values_list('streak_count', flat=True).order_by('-streak_count')[0]  

                percentile = streak/highest*100
        else:
            mood = Mood.objects.all()

        serializer = MoodSerializer(mood, many=True)
        new_serializer_data = list(serializer.data)

        if streak >= 1:
            new_serializer_data.append({'streak': streak})

        if percentile > 50:
            new_serializer_data.append({'percentile': percentile})

        return Response(new_serializer_data)
        

    elif request.method == 'POST':
        serializer = MoodSerializer(data=request.data)
        if serializer.is_valid():
            username = request.user.username if request.user.is_authenticated else serializer.validated_data['streak_user']
            submitted_date = serializer.validated_data['streak_date']
            serializer.save()
            
            if user_streak:
                user_streak = user_streak[0]
                yesterday = submitted_date + timedelta(days=-1)

                if user_streak.last_submit == yesterday:
                    streak_count = user_streak.streak_count + 1

                elif user_streak.last_submit == submitted_date:
                    streak_count = user_streak.streak_count
                else:
                    streak_count = 1
                
                user_streak.streak_count = streak_count
                user_streak.last_submit = submitted_date
                user_streak.save()
            else:
                Streak.objects.create(streak_user=username,streak_count=1,last_submit=submitted_date)


            return Response(serializer.data, status=status.HTTP_201_CREATED)

           
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                


