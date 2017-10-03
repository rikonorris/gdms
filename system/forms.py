import string
from django import forms
from django.contrib.auth import get_user_model


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': '',
                                                  'class': 'form-control input-no-border fo'}))
    password2 = forms.CharField(label='Підтвердіть пароль', widget=forms.PasswordInput(attrs={'placeholder': '',
                                                  'class': 'form-control input-no-border fo'}))

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = True

    class Meta:
        model = get_user_model()
        fields = ('last_name', 'first_name', 'middle_name', 'email', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': '',
                                                 'class': 'form-control input-no-border fo'}),
            'last_name': forms.TextInput(attrs={'placeholder': '',
                                                'class': 'form-control input-no-border fo'}),
            'middle_name': forms.TextInput(attrs={'placeholder': '',
                                                  'class': 'form-control input-no-border fo'}),
            'email': forms.EmailInput(attrs={'placeholder': '',
                                                  'class': 'form-control input-no-border fo'})
        }

    def clean(self):
        super(SignupForm, self).clean()
        if "password1" in self.cleaned_data \
                and "password2" in self.cleaned_data:
            if self.cleaned_data["password1"] \
                    != self.cleaned_data["password2"]:
                self.add_error(
                    'password2',
                    "Паролі повинні співпадати.")
        return self.cleaned_data

    def signup(self, request, user):
        try:
            user.first_name = string.capwords(self.cleaned_data['first_name'].lower())
            user.middle_name = string.capwords(self.cleaned_data['middle_name'].lower())
            user.last_name = string.capwords(self.cleaned_data['last_name'].lower())
            user.username = user.last_name
            user.save()
        except Exception as e:
            raise e

