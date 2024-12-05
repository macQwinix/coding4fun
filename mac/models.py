from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class User(AbstractUser):
  user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user_number = models.PositiveIntegerField(unique=True)
  user_name = models.TextField()


class Incident(models.Model):
  incident_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=255)
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  # Going to be many other fields.
  
  class StateChoices(models.TextChoices):
    INTAKE = 'Intake'
    TEAM_FORMING = 'Team Forming'
    TEAM_FORMED = 'Team Formed'
    DEPLOYED = 'Team Deployed'
    # etc
    CLOSED = 'Closed'

  state = models.CharField(max_length=30
                           , choices=StateChoices.choices
                           , default=StateChoices.INTAKE)

  class Meta:
    ordering = ['-created_at']

  def is_active(self):
    return self.active == True

  def __str__(self):
    return self.title

class Message(models.Model):
  """
  “type”: <statusTypeID>,
	“incident”: “<incidentID>”,
	“sender”: <senderUserID>,
	“sentTS”: “<timestamp of send>”,
  "systemTS": "<timestamp of receive by system>",
	“data”: “<data dependant on status type>”
  """
  class msg_type_choices(models.IntegerChoices):
    chat_msg = 1
    meetup_loc_msg = 2
    status_msg = 3
    image_msg = 4
  
  msg_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  msg_type = models.IntegerField(choices=msg_type_choices.choices)
  incident_id = models.ForeignKey(Incident, on_delete=models.CASCADE)
  sender_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  sent_timestamp = models.DateTimeField()
  system_timestamp = models.DateTimeField(auto_now_add=True)
  data = models.TextField()
  image = models.ImageField(upload_to='images/', blank=True, null=True)

  class Meta:
    ordering = ['-sent_timestamp']

  def __str__(self):
    return str(self.msgID)

