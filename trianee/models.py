from django.db import models
from track.models import Track
from django.urls import reverse
from django.shortcuts import redirect
class Trainee(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    name = models.CharField(max_length=255, db_column='Name')
    image = models.ImageField(upload_to='trianee/images',blank='True', null=True, db_column='Image')
    trackobj = models.ForeignKey(
        Track,
        on_delete=models.CASCADE,
        null=True,
        db_column='TrackID',
    )
    
    def get_absolute_url(self):
        return reverse('trianee:details', kwargs={'pk': self.pk})
    @staticmethod
    def get_list_url():#it depend object
        return reverse('list')
    def getimages(self):
        return f'/media/{self.image}'
    @classmethod
    def create(cls, name, image, track):
        trianeeobj = cls(name=name, image=image, trackobj=Track.objects.get(pk=track))
        trianeeobj.save()
        return trianeeobj 