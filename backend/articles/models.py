from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    body = models.TextField(max_length=64000, blank=True, null=True)

    def __str__(self):
        return self.title
