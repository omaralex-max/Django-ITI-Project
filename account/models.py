from django.db import models
from track.models import *
from django.urls import reverse
class Account(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')  
    name = models.CharField(max_length=255, db_column='Name')
    password = models.CharField(max_length=255, db_column='Password')
    email = models.EmailField(db_column='Email')
    phone = models.CharField(max_length=255, db_column='Phone')
    address = models.CharField(max_length=255, db_column='Address')

    class Meta:
        db_table = 'Account' 
    trackobg = models.ForeignKey(
        'track.Track',
        on_delete=models.CASCADE,
        null=True,
        db_column='TrackID',
    )

    @classmethod
    def get_list_url():
        return reverse('list')
    @classmethod
    def delete_account(cls, id):
        cls.objects.get(id=id).delete()
        cls.get_list_url()