from rest_framework import serializers
from .models import Notice

class NoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice
        # fields = ['title','text','date','number_of_unique_words']
        fields = '__all__'