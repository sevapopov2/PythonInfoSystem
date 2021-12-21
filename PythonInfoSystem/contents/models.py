from django.db import models

class Topic(models.Model):
    topic = models.CharField(max_length=100)
    topic_text = models.TextField()
    def __str__(self):
        return self.topic_text
