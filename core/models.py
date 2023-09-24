from django.db import models


class Note(models.Model):
    title = models.CharField('title', max_length=255)
    content = models.TextField('content')
    done = models.BooleanField('done', default=False)