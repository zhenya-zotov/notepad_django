import datetime

from django.db import models
from users.models import User
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    note_caption = models.CharField(max_length=50)
    note_text = models.TextField(max_length=200)
    note_create_data = models.DateTimeField("date created")
    note_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.note_caption
    
    def was_created_recently(self):
        return self.note_create_data >= timezone.now() - datetime.timedelta(days=1)