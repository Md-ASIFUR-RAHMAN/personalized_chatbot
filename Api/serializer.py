from rest_framework import serializers
from chatbot.models import *

class ChatFaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatFaq
        fields = '__all__'