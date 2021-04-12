from django.db import models

# Create your models here.

class NewsArticle(models.Model):
   id = models.AutoField(primary_key=True)
   shortedUrl = models.CharField(max_length=500 ,default='')
   title = models.CharField(max_length=500 ,default='')
   image = models.URLField(default='')
   publisher = models.CharField(max_length=30,default='')
   pubDate = models.CharField(max_length=20,default='')
   description = models.TextField(max_length=1000,default='')
   link = models.URLField(default='')

   def __str__(self):
       return self.shortedUrl + '-' + self.publisher
   
class SportsNewsArticle(models.Model):
   id = models.AutoField(primary_key=True) 
   shortedUrl = models.CharField(max_length=500 ,default='')
   title = models.CharField(max_length=500,default='')
   image = models.URLField(default='')
   publisher = models.CharField(max_length=30,default='')
   pubDate = models.CharField(max_length=20,default='')
   description = models.TextField(max_length=1000,default='')
   link = models.URLField(default='')

   def __str__(self):
       return self.shortedUrl + '-' + self.publisher

class TechNewsArticle(models.Model):
   id = models.AutoField(primary_key=True) 
   shortedUrl = models.CharField(max_length=500 ,default='')
   title = models.CharField(max_length=500 ,default='')
   image = models.URLField(default='')
   publisher = models.CharField(max_length=30,default='')
   pubDate = models.CharField(max_length=20,default='')
   description = models.TextField(max_length=1000,default='')
   link = models.URLField(default='')

   def __str__(self):
       return self.shortedUrl + '-' + self.publisher

class ScienceNewsArticle(models.Model):
   id = models.AutoField(primary_key=True) 
   shortedUrl = models.CharField(max_length=500 ,default='')
   title = models.CharField(max_length=500 ,default='')
   image = models.URLField(default='')
   publisher = models.CharField(max_length=30,default='')
   pubDate = models.CharField(max_length=20,default='')
   description = models.TextField(max_length=1000,default='')
   link = models.URLField(default='')

   def __str__(self):
       return self.shortedUrl + '-' + self.publisher

class HealthNewsArticle(models.Model):
   id = models.AutoField(primary_key=True) 
   shortedUrl = models.CharField(max_length=500,default='')
   title = models.CharField(max_length=500 ,default='')
   image = models.URLField(default='')
   publisher = models.CharField(max_length=30,default='')
   pubDate = models.CharField(max_length=20,default='')
   description = models.TextField(max_length=1000,default='')
   link = models.URLField(default='')

   def __str__(self):
       return self.shortedUrl + '-' + self.publisher

class BusinessNewsArticle(models.Model):
   id = models.AutoField(primary_key=True) 
   shortedUrl = models.CharField(max_length=500 ,default='')
   title = models.CharField(max_length=500 ,default='')
   image = models.URLField(default='')
   publisher = models.CharField(max_length=30,default='')
   pubDate = models.CharField(max_length=20,default='')
   description = models.TextField(max_length=1000,default='')
   link = models.URLField(default='')

   def __str__(self):
       return self.shortedUrl + '-' + self.publisher

class EntertainmentNewsArticle(models.Model):
   id = models.AutoField(primary_key=True) 
   shortedUrl = models.CharField(max_length=500,default='')
   title = models.CharField(max_length=500 ,default='')
   image = models.URLField(default='')
   publisher = models.CharField(max_length=30,default='')
   pubDate = models.CharField(max_length=20,default='')
   description = models.TextField(max_length=1000,default='')
   link = models.URLField(default='')

   def __str__(self):
       return self.shortedUrl + '-' + self.publisher