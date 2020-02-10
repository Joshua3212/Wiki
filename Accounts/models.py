from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    picture = models.CharField(max_length=1000, default='https://images.pexels.com/photos/417173/pexels-photo-417173.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500')
    mainContent = models.CharField(max_length=20000)
    user = models.CharField(max_length=100)
    date = models.CharField(max_length=10 , default='00-00-0000')
    url = models.CharField(max_length=200, default='none')

    def __str__(self):
        return self.title
