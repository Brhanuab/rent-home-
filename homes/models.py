from django.db import models


class home(models.Model):
    name_owner=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    price=models.IntegerField()
    bf_image=models.ImageField(upload_to='home/')
    bac_image=models.ImageField(upload_to='home/')
    numberof_home=models.IntegerField()
    phone_owner=models.IntegerField(default=0)
    


class renter(models.Model):
    home_number=models.IntegerField()
    user_name=models.CharField(max_length=100 ,default=0)
    your_contact=models.IntegerField()
    

# Create your models here.
