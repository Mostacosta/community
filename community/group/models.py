from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class groups (models.Model):
    name = models.CharField(max_length=50)
    longtude = models.DecimalField(max_digits=30, decimal_places=22)
    latitude = models.DecimalField(max_digits=30, decimal_places=22)

    def __str__(self):
        return self.name

class posts (models.Model):
    post = models.CharField(max_length=150)
    group = models.ForeignKey(groups,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.post[0:20]

class comments (models.Model):
    comment = models.CharField(max_length=300)
    post = models.ForeignKey(posts,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment[0:20]




    
