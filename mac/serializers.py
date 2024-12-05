from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Message, Incident, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'userID',
            'user_number', 
            'user_name',
        )
        
class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = (
            'incidentID', 
            'title', 
            'body', 
            'created_at', 
            'updated_at',
        )

class MessageSerializer(serializers.ModelSerializer):
    parent = serializers.HyperlinkedRelatedField(view_name='incident-detail', read_only=True)
    class Meta:
        model = Message
        fields = (
            'msg_id',
            'msg_type', 
            'incident_id', 
            'sender_id', 
            'sent_timestamp', 
            'system_timestamp', 
            'data',
        )

    def validate_msg_type(self, value):
        pass
        # write real validators

