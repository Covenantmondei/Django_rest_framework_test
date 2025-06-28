from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title
    
class Logistics(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)



class UserClass(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)


class Profile(models.Model):
    user = models.OneToOneField(UserClass, related_name="user_profile", on_delete=models.CASCADE)
    dob = models.DateField()