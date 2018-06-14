from django.forms import ModelForm
from .models import offer

# Create the form class.
class offer_form(ModelForm):
    class Meta:
        model = offer
        exclude = ['worker','status','order','sign',]
        # fields = ['price', 'many']