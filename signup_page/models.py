#from django.db import models
#from django.contrib.auth.models import User



# Create your models here.
#from django.shortcuts import render, redirect
#from .forms import SignupForm  # Import your SignupForm here
#from .models import Signup


#from django.db import models

#class Signup(models.Model):
   # username = models.CharField(max_length=255)
    #emailaddress = models.EmailField(max_length=255)
    #password = models.CharField(max_length=255)  
    #confirm_password = models.CharField(max_length=255)


#class Login(models.Model):
 #   username = models.CharField(max_length=255)
  #  password = models.OneToOneField(User, on_delete=models.CASCADE)




#def __str__(self):
   # return f"{self.username} {self.emailaddress}"
from django.db import models

class Signup(models.Model):
    username = models.CharField(max_length=255)
    emailaddress = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)  
    confirm_password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username} {self.emailaddress}"

class Login(models.Model):
    user = models.ForeignKey(Signup, on_delete=models.CASCADE)
    # Other login-related fields can be added here

    def __str__(self):
        return self.user.username
