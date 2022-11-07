from email.headerregistry import Address
from django import forms

STATES = (
    ("1","AC"),
    ("2","AL"),
    ("3","AP"),
    ("4","AM"),
    ("5","BA"),
    ("6","CE"),
    ("7","DF"),
    ("8","ES"),
    ("9","GO"),
    ("10","MA"),
    ("11","MT"),
    ("12","MS"),
    ("13","MG"),
    ("14","PA"),
    ("15","PB"),
    ("16","PR"),
    ("17","PE"),
    ("18","PI"),
    ("19","RJ"),
    ("20","RN"),
    ("21","RS"),
    ("22","RO"),
    ("23","RR"),
    ("24","SC"),
    ("25","SP"),
    ("26","SE"),
    ("27","TO"),
)

class NewData(forms.Form):
    username = forms.CharField(max_length=50)
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    address = forms.CharField()
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    cep = forms.CharField()
    check = forms.BooleanField(required=False)
