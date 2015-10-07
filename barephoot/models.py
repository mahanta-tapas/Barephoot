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
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    timings = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

class Events(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    day = models.CharField(max_length=10)
    time = models.CharField(max_length=10)

    def __unicode__(self):
        return (self.name)

