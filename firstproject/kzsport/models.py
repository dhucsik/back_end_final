from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{7,11}$')

# Create your models here.

class Sportsman(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = models.TextField(null=True)

    @classmethod
    def isYoung(cls, sp_age):
        if sp_age < 30:
            return "Yes"
        else:
            return "No" 

class University(models.Model):
    university_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField(null=True)

class City(models.Model):
    city_name = models.CharField(max_length=200)
    description = models.TextField(null=True)

    @classmethod
    def isMegapolis(cls, population):
        if population > 1000000:
            return True
        else:
            return False

class Tradition(models.Model):
    title = models.CharField('Atau', max_length=50)
    intro = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Sipat')
    famous = models.CharField('Name', max_length=40)
    history = models.TextField('Tarih')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

class Food(models.Model):
    title = models.CharField('Atau', max_length=50)
    full_text = models.TextField('Sipat')
   
    
    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 30, default='anonymous')
    feedback = models.TextField(default = 'That was amazing!!!')

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    maleF = models.CharField(max_length=10)
    number = models.CharField("Phone Number", validators=[phone_regex], max_length=11, blank=True)

    def __str__(self):
        return self.username