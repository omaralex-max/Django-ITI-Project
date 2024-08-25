from django import forms
from track.models import Track
class addTrianee(forms.Form):
    name=forms.CharField(required=True, max_length=300)
    image=forms.ImageField(required=False,label='Upload Image')
    trackid=forms.ChoiceField(choices=Track.getall())