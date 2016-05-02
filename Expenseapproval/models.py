from django.db import models

# Create your models here.


class Expenses(models.Model):

    id=models.AutoField(primary_key=True)
    employee_Name=models.CharField(max_length=50,null=True)
    Category=models.CharField(max_length=10,null=True)
    Date=models.DateField(null=True,blank=True)
    Ammount = models.IntegerField(null=True)
    status=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.employee_Name

class Users(models.Model):

    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username

