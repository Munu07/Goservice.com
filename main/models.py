from django.db import models

class Service(models.Model):
    profession_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.profession_name



