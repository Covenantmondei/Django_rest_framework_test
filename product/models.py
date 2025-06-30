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

class School(models.Model):
    name = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)

class Student(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="school")

class UserClass(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)


class Profile(models.Model):
    user = models.OneToOneField(UserClass, related_name="user_profile", on_delete=models.CASCADE)
    dob = models.DateField()
    marital_status = models.CharField(max_length=255, null=True, blank=True)

class Courses(models.Model):
    title = models.CharField(max_length=255)
    students = models.ManyToManyField(Student, related_name="offered")

# name = ["covenant", "david", "imo", "victory", "idara", "monday", "victor", "dell", "wisdom", "brown", "micheal", "james", "joseph", "john", "peter", "paul", "stephen", "daniel", "samuel", "solomon"]

# id = [1, 2, 3, 4, 5]=