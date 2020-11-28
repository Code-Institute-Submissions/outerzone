from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = {'user', }

    def __init__(self, *args, **kwargs):
        """ Add placeholders, classes, remove auto-gen labels,
        set autofocus on first field """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Postal Address 1',
            'default_street_address2': 'Postal Address 2',
            'default_town_or_city': 'Town or City',
            'default_postcode': 'Postcode',
            'default_county': 'County',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form'
            self.fields[field].label = False
