from django import forms

from .models import contacte,Billing


class contacteForm(forms.ModelForm):
    class Meta:
        model = contacte
        fields = ['fullname','emailaddress','message']     

from django import forms


class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['full_name', 'address', 'city', 'postal_code', 'country']
