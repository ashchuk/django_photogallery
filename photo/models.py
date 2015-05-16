# coding=utf-8
from django.db import models
from sorl.thumbnail import ImageField
from django.utils import timezone

'''
# It's a category class
# Use it, then need division into albums

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category_thumbnail = ImageField(upload_to='category_thumbnails')

    def __unicode__(self):
        return self.name
'''


class Album(models.Model):
    # Here's a category-album relation
    #
    # category = models.ForeignKey(Category)
    #

    name = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateTimeField('Publishing date', default=timezone.now())
    album_thumbnail = ImageField(upload_to='album_thumbnails')

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=100)
    image = ImageField(upload_to='photos')
    caption = models.CharField(max_length=250, blank=True)
    pub_date = models.DateTimeField('Publishing date', default=timezone.now())

    def __unicode__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Publishing date', default=timezone.now())
    message = models.TextField()

    def __unicode__(self):
        return self.name