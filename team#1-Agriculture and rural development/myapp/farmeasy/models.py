from django.db import models


class Grain(models.Model):
    grain_name = models.CharField(max_length=100)
    grain_type = models.CharField(max_length=100)
    grain_price = models.CharField(max_length=100)
    grain_date = models.DateField(default='2019-10-05')
    grain_image = models.ImageField(default='None',upload_to='images/')

    def __str__(self):
        return self.grain_name

class farmer(models.Model):
    grain = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    date = models.DateField(default='2019-10-05')
    price = models.CharField(max_length=100)
    image = models.ImageField(default='None',upload_to='images/')

     
