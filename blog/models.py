from django.db import models
from datetime import datetime
class posts(models.Model):
    title = models.CharField(max_length=1000)
    body =  models.TextField(blank=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100)
    likes = models.IntegerField()
    date = models.DateTimeField(default=datetime.now,blank=True)


    def __str__(self):
        return self.title





