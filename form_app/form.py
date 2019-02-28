from django import forms


class Form_demo(forms.Form):

    fullName = forms.CharField(max_length=150)
    email = forms.CharField()
    phoneNumber = forms.CharField(max_length=15)
    company = forms.CharField(max_length=30)
    message = forms.CharField(max_length=200)

    def Send(self):
        pass