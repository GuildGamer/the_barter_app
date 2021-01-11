from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    author = models.OneToOneField(User, related_name="author_messages", on_delete=models.CASCADE)
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
    
    def last_10_messages(self):
        return Message.objects.order_by('-time_stamp').all()[:10]

