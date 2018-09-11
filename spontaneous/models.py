from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    date = models.DateField()
    event_url = models.URLField()

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 20)
    INTERESTS = (
        ('1', 'Tech'),
        ('2', 'Sports'),
        ('3', 'Video Games'),
        ('4', 'Movies')
        #list other interests
    )
    interest = models.CharField(
        max_length = 1,
        choices = INTERESTS,
        default = '1'
    )
    events = models.ManyToManyField(Event)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')


