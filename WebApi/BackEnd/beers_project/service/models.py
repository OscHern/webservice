from django.db import models

# Create your models here.

class Kind(models.Model):
    IdKind = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Beer(models.Model):
    IdBeers = models.AutoField(primary_key=True)
    percentage = models.FloatField(null=False)
    brand = models.CharField(max_length=50)
    name =  models.CharField(max_length=50)
    type =  models.PositiveIntegerField(null=False)
    detail = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class Selection(models.Model):
   # Id = models.AutoField(primary_key=True)
    IdBeer = models.PositiveIntegerField(null=False)
    IdUser = models.PositiveIntegerField(null=False)
    dateLog = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Id_Beer : " + str(self.IdBeer) + "- Id_User" +str(self.IdUser)


class User(models.Model):
    Id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=50)
    password =  models.CharField(max_length=50)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class UpTake(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    percentage = models.FloatField(null=False)
    brand = models.CharField(max_length=50)
    name =  models.CharField(max_length=50)
    type =  models.CharField(max_length=50)
    cantida = models.IntegerField(null=False)
    username = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.name
    
    class Meta:   
        managed = False
        db_table = 'service_uptake'