from django.db import models

class ChatUser(models.Model): 
    username = models.CharField(max_length=255)
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username