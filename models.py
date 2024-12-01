from django.db import models

# Create your models here.
class registration(models.Model):
    student_name=models.CharField(max_length=30)
    parent_name=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.EmailField()
    
