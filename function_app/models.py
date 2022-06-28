# Create model for class
from django.db import models


class Student(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    number = models.CharField(max_length=16)
    image = models.FileField(null=True, blank=True, upload_to='images/')
    qualification_choices = [
        ('10th', '10th'),
        ('12th', '12th'),
        ('ug', 'ug'),
        ('pg', 'pg')
    ]
    qualification = models.CharField(
        max_length=4,
        choices=qualification_choices,
        default=0,
    )
    message = models.TextField()

