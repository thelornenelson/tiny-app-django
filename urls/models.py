from django.db import models
from django.utils import timezone
import random

class Url(models.Model):

    @staticmethod
    def generate_short_url():
        possible = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz23456789"
        short_url = ""
        for i in range(5):
            short_url += random.choice(possible)
        return short_url

    short_url = models.CharField(max_length=8, default=generate_short_url)
    long_url = models.TextField()
    times_visited = models.PositiveIntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return "{} : {} - {} visits".format(self.short_url, self.long_url, self.times_visited)






    # "b2xVn2": {longURL: "http://www.lighthouselabs.ca", userId: "geg7aa", date:  new Date(2018, 1, 5, 10, 5), redirects: 3, updated: true},
