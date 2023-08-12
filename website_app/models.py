from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=40)
    mobile=models.BigIntegerField()
    email=models.EmailField()
    course=models.CharField(max_length=20)

    def __str__(self):
        return self.name

