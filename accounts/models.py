from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    photo = models.ImageField(default='default.jpeg', upload_to='passports/')
    gender_select = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(choices=gender_select, max_length=6)
    employee_select = (
        ('admin', 'Admin'),
        ('employee', 'Employee'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    employee_type = models.CharField(choices=employee_select, max_length=15)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)