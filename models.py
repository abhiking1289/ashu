
from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')

# Create your models here.
AUDIO_CHOICES = (
            ('Select Caption', "Select Caption"),
            ('ENGLISH' , "English"),
            ('Español', "Español"),
            ('Português', "Português"),
            ('Italiano',"Italiano"),
            ('Français', "Français"),
            ('Polski', "Polski"),
            ('Deutsch', "Deutsch"),
            ('Bahasa Indonesia',"Bahasa Indonesia"),
            ('ภาษาไทย', "ภาษาไทย"),
            ('हिन्दी',"हिन्दी"),
            ('Tamil',"Tamil"),
            ('मराठी',"मराठी"),
            ('Telugu',"Telugu"),
        )
LEVEL_CHOICES = (
    ('Select Level',"Select Level"),
    ('Beginner',"Beginner"),
    ('Intermediate',"Intermediate"),
    ('Expert',"Expert"),
)
class Destination(models.Model):
    City =  models.CharField(max_length=100)
    img = models.ImageField(upload_to ='pics')  
    Description =  models.TextField()
    Arrival =  models.IntegerField()
    Budjet =  models.IntegerField()
class create_new_course(models.Model):
    class Basic_Information(models.Model):
        Course_title = models.CharField(max_length=60)
        Short_Description = models.TextField()
        Course_Description = models.TextField()
        What_will_students_learn_in_your_course = models.TextField()
        Requirements = models.TextField()
        Course_level = models.CharField(
            max_length= 30,
            choices= LEVEL_CHOICES,
            default = 'Select Level'
        )
        Close_Caption = models.CharField(
            max_length= 30,
            choices= AUDIO_CHOICES,
            default = 'Select Caption'
        )
        Audio_Language = models.CharField(
            max_length= 30,
            choices= AUDIO_CHOICES,
            default = 'Select Caption'
        )
        Course_Category = models.TextChoices
