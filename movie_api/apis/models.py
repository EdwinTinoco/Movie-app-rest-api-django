from django.db import models

class Movies(models.Model):
   title = models.CharField(max_length=100, blank=False)
   description = models.TextField(blank=True, null=True)
   genre = models.CharField(max_length=50)
   image_url = models.CharField(max_length=500)
   year_release = models.PositiveIntegerField(blank=False)
   classification = models.CharField(max_length=50)
   duration = models.CharField(max_length=20)

   class Meta:
      db_table = 'movies'
      ordering = ['year_release']

class Comments(models.Model):
   comment = models.TextField(blank=False)
   created = models.CharField(max_length=30)
   movie_id = models.IntegerField()
   user_id = models.IntegerField()

   class Meta:
      db_table = 'comments'

class Rates(models.Model):
   rated = models.IntegerField()
   movie_id = models.IntegerField()

   class Meta:
      db_table = 'rates'


class Users(models.Model):
   name = models.CharField(max_length=100, blank=False)
   email =  models.CharField(max_length=200, blank=False)
   password = models.CharField(max_length=20, blank=False)

   class Meta:
      db_table = 'users'

