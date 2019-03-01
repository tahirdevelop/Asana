from django import forms


class Form_demo(forms.Form):

    fullName = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'placeholder': 'Имя', 'class': 'form-control', 'id': 'id_fullName'}))

    email = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'E-mail', 'class': 'form-control', 'id': 'id_email'}))

    phoneNumber = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs={'placeholder': 'Номер телефона', 'class': 'form-control', 'id': 'id_phoneNumber'}))

    company = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'placeholder': 'Компания', 'class': 'form-control', 'id': 'id_company'}))

    message = forms.CharField(max_length=200, widget=forms.Textarea(
        attrs={'placeholder': 'Сообщение', 'class': 'form-control', 'rows': 3, 'id': 'id_message'}))

    def __str__(self):
        return f"Имя: {self.cleaned_data['fullName']} \n" \
               f"E-mail: {self.cleaned_data['email']} \n" \
               f"Номер телефона: {self.cleaned_data['phoneNumber']} \n" \
               f"Компания: {self.cleaned_data['company']} \n" \
               f"Сообщение: {self.cleaned_data['message']}"