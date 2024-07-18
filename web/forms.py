from django import forms

class ContactFormForm(forms.Form):
  email = forms.EmailField(label="Correo")
  name = forms.CharField(max_length=50, label="Nombre")
  message = forms.CharField(label="Mensaje")