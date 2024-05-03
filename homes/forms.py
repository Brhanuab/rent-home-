from django import forms
from .models import home,renter

class homecreationForm(forms.ModelForm):
    class Meta:
        model=home
        fields=['name_owner','location','price','bf_image','bac_image','name_owner','numberof_home','phone_owner']


class rentercreationForm(forms.ModelForm):
    class Meta:
        model=renter
        fields=['home_number','your_contact','user_name']



