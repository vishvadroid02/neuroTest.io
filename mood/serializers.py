from rest_framework import serializers
from .models import Mood


#serializes the Model

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        exclude = ()