from django.forms import ModelForm
from .models import worker

# Create the form class.
class often_form(ModelForm):
    class Meta:
        model = often
        exclude = ['worker',]
        # fields = ['price', 'many']