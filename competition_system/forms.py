from django.forms import ModelForm
from .models import worker

# Create the form class.
class offer_form(ModelForm):
    class Meta:
        model = offer
        exclude = ['worker','status',]
        # fields = ['price', 'many']