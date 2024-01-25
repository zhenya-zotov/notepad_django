from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_nickname = models.CharField(max_length=25)
    user_password = models.CharField(max_length=25, default='test_password')
    user_mail = models.EmailField(max_length=255)
