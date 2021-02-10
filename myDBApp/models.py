from django.db import models
from django.urls import reverse
# Create your models here.

class College(models.Model):
    name = models.CharField(max_length = 10)
    director_name = models.CharField(max_length = 10)
    location = models.CharField(max_length = 10)
    courses = models.CharField(max_length = 10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myDBApp:list')

class Student(models.Model):
    first_name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length = 10)
    phone_number = models.IntegerField()
    roll_number = models.IntegerField()
    course = models.CharField(max_length = 10)
    college = models.ForeignKey(College,related_name = 'students', on_delete = models.PROTECT)

    def __str__(self):
        return self.first_name + self.last_name

    def get_absolute_url(self):
        return reverse('myDBApp:list')
