from django.db import models
import uuid
# Create your models here.

class Tutor(models.Model):
    tutor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tutor_first_name = models.CharField(max_length=128)
    tutor_last_name = models.CharField(max_length=128)
    tutor_email = models.EmailField(max_length=254, unique=True)
    tutor_booking_status = models.BooleanField()
    is_student = models.BooleanField()
    university_name = models.CharField(max_length=200)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)    #max_digits includes number of decimal places
    #tags = TaggableManager() #look at documentation https://pypi.python.org/pypi/django-taggit
    availability = models.BooleanField()
    tutor_intro = models.TextField()

    def __str__(self):
        return self.tutor_first_name

class Student(models.Model):
    #student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_first_name = models.CharField(max_length=128)
    student_last_name = models.CharField(max_length=128)
    student_email = models.EmailField(max_length=254, unique=True)
    student_booking_status = models.BooleanField()
    is_tutor = models.BooleanField()
    tutor = models.ForeignKey(Tutor)


    def __str__(self):
        return self.student_first_name
