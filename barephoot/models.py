from django.db import models
#from pygments.lexers import  get_lexer_by_name
#from pygments.formatters.html import HtmlFormatter
#from pygments import highlight
from django.contrib.auth.models import User


class Movdata(models.Model):
    movie_name = models.CharField(max_length=50)
    theatre = models.CharField(max_length=50)
    timing = models.CharField(max_length=10)
    owner = models.ForeignKey('auth.user',related_name='barephoot')

class TheatreDetail(models.Model):
    theatre = models.CharField(max_length=200,unique=True)
    lat = models.FloatField()
    long = models.FloatField()
    rating = models.FloatField()
    price2 = models.FloatField()



class Restdata(models.Model):
    name = models.CharField(max_length=200,unique=True)
    lat = models.FloatField()
    long = models.FloatField()
    rating = models.FloatField()
    price2 = models.FloatField()
    owner = models.ForeignKey('auth.user',related_name='barephoot2')


class PlacestoVisit(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=200)
    lat = models.FloatField()
    long = models.FloatField()
    timings = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    rating = models.CharField(max_length=50)
    review_count = models.CharField(max_length=50)

class Events(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=200)
    lat = models.FloatField()
    long = models.FloatField()
    day = models.CharField(max_length=200)
    time = models.CharField(max_length=200)

    def __unicode__(self):
        return (self.name)

