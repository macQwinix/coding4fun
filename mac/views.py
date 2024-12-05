#from django.http import HttpResponse, HttpRequest, JsonResponse
#from django.contrib.auth.models import Group, User
#from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from mac.serializers import UserSerializer, IncidentSerializer, MessageSerializer
from mac.models import Message, Incident, User


@api_view(['GET'])
def incident_list(request):
    incidents = Incident.objects.all()
    serializer = IncidentSerializer(incidents, many=True)
    return Response({
        'incidents': serializer.data
        })


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class IncidentViewSet(viewsets.ModelViewSet):
#     queryset = Incident.objects.all().order_by('-created_at')
#     serializer_class = IncidentSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class MessageViewSet(viewsets.ModelViewSet):
#     queryset = Message.objects.all().order_by('-sentTS')
#     serializer_class = MessageSerializer
#     permission_classes = [permissions.IsAuthenticated]

# def authenticate(request: HttpRequest):
#     resp = JsonResponse({"userID":756})
#     return resp