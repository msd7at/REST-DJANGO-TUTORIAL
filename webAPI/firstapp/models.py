from django.db import models

# Create your models here.
class Person(models.Model):
    Name= models.CharField(max_length=30)
    Birthday=models.DateField()
    Age=models.IntegerField()

    def __str__(self):
        return "{}".format(self.Name)