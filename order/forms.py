from django.forms import ModelForm
from .models import order

# Create the form class.
class order_form(ModelForm):
    class Meta:
        model = order
        exclude = ['client',]
        # fields = ['price', 'many']