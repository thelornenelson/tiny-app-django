from django.db import models

class Url(models.Model):
    short_url = models.CharField(max_length=8)
    long_url = models.TextField()
    times_visited = models.PositiveIntegerField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "{} : {} - {} visits".format(self.short_url, self.long_url, self.times_visited)





    # "b2xVn2": {longURL: "http://www.lighthouselabs.ca", userId: "geg7aa", date:  new Date(2018, 1, 5, 10, 5), redirects: 3, updated: true},
