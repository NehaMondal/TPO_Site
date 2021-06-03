from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
# Create your models here.


class UserInfoModel(models.Model):
    COURSE = (
        ('BTECH', 'bachelors_tech'),
        ('MTECH', 'masters_tech'),
        ('MBA', 'masters_management'),
        ('BBA', 'bachelors_business'),
        ('BCA', 'bachelors_application')
    )
    BRANCH = (
        ('CS', 'computer_science'),
        ('ME', 'mechanical'),
        ('EE', 'electrical'),
        ('ECE', 'electronics_comm'),
        ('IT', 'information_technology')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=10,unique=True)
    passing_year = models.PositiveIntegerField(null=False)
    branch= models.CharField(max_length=10,choices=BRANCH, default='CS', blank = True)
    course = models.CharField(max_length=5,choices=COURSE, default='BTECH')
    college = models.CharField(max_length=100, blank=False)
    dob = models.DateField()
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    father_number = models.PositiveSmallIntegerField(null=False)
    mother_number = models.PositiveSmallIntegerField(null=False)
    phone_number = models.PositiveSmallIntegerField(null=False)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=20)
    pincode = models.PositiveSmallIntegerField(null=False)
    state = models.CharField(max_length=20)
    alternate_gmail = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, default="", blank=True, null=True)

    def __str__(self):
        return self.user.username

