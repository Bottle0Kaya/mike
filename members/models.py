from django.db import models
from django.contrib.auth.models import User



#class plant_photos(models.Model):
#    plant_photos = 

class plant_inf(models.Model):
    Plant_name = models.CharField('Plant Name', max_length=120)
    Color = models.CharField(max_length=20)
    Plant_type = models.CharField('Plant_type', max_length=10, blank=True)
    Origin = models.CharField ('Origin', max_length=100, blank=True)

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=100)
    zip_code =models.CharField('Zip Code', max_length=100)
    phone = models.CharField('Contact Phone', max_length=10, blank=True)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField('Email Address', blank=True)

    def __str__(self):
        return self.name

class MyClubUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Event(models.Model):
    name = models.CharField('event name', max_length=100)
    event_date = models.DateTimeField('event date')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, null=True)
    #venue = models.CharField(max_length=100)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name

