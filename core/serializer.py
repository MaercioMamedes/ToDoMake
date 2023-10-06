import datetime

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import Note
import datetime


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class NoteSerializerHard(serializers.Serializer):
    note_id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    content = serializers.CharField()
    done = serializers.BooleanField()

    def create(self, validated_data):
        now = datetime.datetime.now()
        time_stamp = now.strftime("%f")
        validated_data['note_id'] = int(time_stamp)
        return validated_data

