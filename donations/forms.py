from django import forms
from .models import Donation

from django import forms
from .models import Donation

# A form for collecting user donations based on the Donation model.
class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'amount', 'message']
        
        # I customized the default field lables and forms to make it clearer for the users.
        labels = {
            'name': 'Name (Optional)',
            'amount': 'Donation Amount (USD)',
            'message': 'Why are you donating? (Optional)',
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3}),
        }
