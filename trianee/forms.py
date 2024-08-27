from django import forms
from .models import *
from track.models import Track
class addTrianee(forms.Form):
    
    name=forms.CharField(required=True, max_length=300, widget=forms.TextInput(attrs={'class':'','color':''}))
    imag=forms.ImageField(required=False,label='Upload Image')
    track=forms.ChoiceField(choices=Track.getall())

class AddTraineeModel(forms.ModelForm):
    track=forms.ChoiceField(choices=Track.getall())
    class Meta:
        model = Trainee
        fields = '__all__'
        exclude = ['trackobj']
        help_texts = {
            
            'track': 'Track is required',
        }
        error_messages = {
            'name': {
                'required': 'Name is required',
            }
        }