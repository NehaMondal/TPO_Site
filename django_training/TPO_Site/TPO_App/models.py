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
    roll_no = models.CharField(max_length=10)
    passing_year = models.PositiveIntegerField(null=True, default="2022")
    branch= models.CharField(max_length=10,choices=BRANCH, default='CS', blank = False)
    course = models.CharField(max_length=5,choices=COURSE, default='BTECH')
    college = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    father_number = models.PositiveSmallIntegerField(null=True)
    mother_number = models.PositiveSmallIntegerField(null=True)
    phone_number = models.PositiveSmallIntegerField(null=True)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=20)
    pincode = models.PositiveSmallIntegerField(null=True)
    state = models.CharField(max_length=20)
    alternate_gmail = models.EmailField()
    gender = models.CharField(max_length=10, default="", blank=True, null=True)

    def __str__(self):
        return self.user.username

class UserMarksModel(models.Model):
    user = models.ForeignKey(UserInfoModel, on_delete=models.CASCADE, related_name="marks")
    tenth_obt_marks = models.PositiveSmallIntegerField()
    tenth_total_marks = models.PositiveSmallIntegerField()
    twelve_obt_marks = models.PositiveSmallIntegerField()
    twelve_total_marks = models.PositiveSmallIntegerField()
    jee_rank = models.PositiveSmallIntegerField(null=True)
    first_sem_marks = models.PositiveSmallIntegerField(null=True)
    second_sem_marks = models.PositiveSmallIntegerField(null=True)
    third_sem_marks = models.PositiveSmallIntegerField(null=True)
    fourth_sem_marks = models.PositiveSmallIntegerField(null=True)
    fifth_sem_marks = models.PositiveSmallIntegerField(null=True)
    sixth_sem_marks = models.PositiveSmallIntegerField(null=True)
    seventh_sem_marks = models.PositiveSmallIntegerField(null=True)
    supplees = models.PositiveSmallIntegerField(null=True)
    aggregates = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.user.username


class TrainingInfoModel(models.Model):
    Mode = (
        ('Offline', 'Offline'),
        ('Online', 'Online')
    )
    user = models.ForeignKey(UserInfoModel, on_delete=models.CASCADE, related_name="training_detail")
    technology= models.CharField(max_length=80)
    project = models.CharField(max_length=50)
    training_mode= models.CharField(max_length=7,choices=Mode, default="Offline", blank=False)
    institute_name = models.CharField(max_length=40)
    institute_address = models.CharField(max_length=100)
    institute_number = models.PositiveSmallIntegerField(null=True, blank=True)
    training_duration = models.PositiveSmallIntegerField(null = False)

    def __str__(self):
        return self.user.username



class DocumentsModel(models.Model):
    user = models.ForeignKey(UserInfoModel, on_delete=models.CASCADE, related_name="document_proof")
    tenth_dmc = models.FileField(upload_to="documents/tenth_dmc")
    twelvth_dmc = models.FileField(upload_to="documents/twelvth_dmc")
    first_sem_dmc = models.FileField(upload_to="documents/first_sem")
    second_sem_dmc = models.FileField(upload_to="documents/second_sem")
    third_sem_dmc = models.FileField(upload_to="documents/third_sem")
    fourth_sem_dmc = models.FileField(upload_to="documents/fourth_sem")
    fifth_sem_dmc = models.FileField(upload_to="documents/fifth_sem")
    sixth_sem_dmc = models.FileField(upload_to="documents/sixth_sem")
    seventh_sem_dmc = models.FileField(upload_to="documents/seventh_sem")

    def __str__(self):
        return self.user.username
