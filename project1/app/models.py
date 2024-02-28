from django.db import models

# Create your models here.


class users(models.Model):
    status_choice=(('accepted','accepted'),('rejected','rejected'),('pending','pending'))
    name = models.CharField(max_length = 200)
    dob = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 200)
    place = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    status=models.CharField(choices=status_choice,default='pending',max_length=200)
    user_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name