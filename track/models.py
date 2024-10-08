from django.db import models

# Create your models here.
class Track(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    title = models.CharField(max_length=255, db_column='Title')
    
    @classmethod
    def getall(cls):

        return [(track.id, track.title) for track in cls.objects.all()]