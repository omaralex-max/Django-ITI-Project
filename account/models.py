from django.db import models
from track.models import *
# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')  # Corrected 'primarykey' to 'primary_key'
    name = models.CharField(max_length=255, db_column='Name')
    password = models.CharField(max_length=255, db_column='Password')
    email = models.EmailField(db_column='Email')
    phone = models.CharField(max_length=255, db_column='Phone')
    address = models.CharField(max_length=255, db_column='Address')

    class Meta:
        db_table = 'Account'  # Optional: Specifies the actual database table name
    trackobg = models.ForeignKey(
        'track.Track',
        on_delete=models.CASCADE,
        null=True,
        db_column='TrackID',  # Optional: Specifies the field in the database table that represents the foreign key
    )