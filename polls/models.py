from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(max_length=250)


def __str__(self):
    return self.question
