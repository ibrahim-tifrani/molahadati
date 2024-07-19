from django.db import models
class note1(models.Model):
    name1=models.CharField(blank=True,max_length=50,null=False)
    year_of_study1=models.CharField(blank=False,max_length=15,null=False)
    notes1=models.TextField()
    def __str__(self):
        return self.name1
class note2(models.Model):
    name2=models.CharField(blank=True,max_length=50,null=False)
    year_of_study2=models.CharField(blank=False,max_length=15,null=False)
    notes2=models.TextField()
    def __str__(self):
        return self.name2
class note3(models.Model):
    name3=models.CharField(blank=True,max_length=50,null=False)
    year_of_study3=models.CharField(blank=False,max_length=15,null=False)
    notes3=models.TextField()
    def __str__(self):
        return self.name3
class note4(models.Model):
    name4=models.CharField(blank=True,max_length=50,null=False)
    year_of_study4=models.CharField(blank=False,max_length=15,null=False)
    notes4=models.TextField()
    def __str__(self):
        return self.name4
class notif(models.Model):
    name_of_teacher=models.CharField(max_length=100,default="notification")
    conversation=models.TextField(blank=True)
    def __str__(self):
        return self.name_of_teacher
# Create your models here.
