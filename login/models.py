from django.db import models

class Signin(models.Model):
    id = models.AutoField(primary_key=True)
    parent_child_name= models.CharField(max_length=30, blank=True,null=False)
    child_name = models.CharField(max_length=50, blank=True,null=False)
    typ = models.CharField(max_length=10)
    gmail = models.EmailField()
    phone = models.CharField(max_length=10)
    def __str__(self):
        return self.child_name 

# Create your models here.
