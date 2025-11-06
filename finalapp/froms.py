from django import forms
from .models import student
from.models import contact
from .models import contacte

class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'age', 'grade']


class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['email', 'message']


class contacteForm(forms.ModelForm):
    class Meta:
        model = contacte
        fields = ['fullname','emailaddress','message']     