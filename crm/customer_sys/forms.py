from django import forms
from .models import Contact, Note, Party
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import PrependedText
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "address",
            "status",
            "last_contact",
            "bg_info",
            ]

        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "last_contact": "Date Last Contacted",
            "bg_info": "Background Info",
        }

        widgets = {
        "last_contact": forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        "bg_info": forms.Textarea(attrs={'rows':2}),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            "body",
        ]

        labels = {
            'body':"New Note:",
        }

        widgets = {
            'body': forms.Textarea(attrs={'rows':2}),
        }

class PartyForm(forms.ModelForm):
    class Meta:
        model = Party

        #guest = forms.MultipleChoiceField(queryset=User.contacts)

        fields = [
            "host",
            "start_date",
            "total",
            "link",
            "guest",
        ]

        widgets = {
        "start_date": forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        "guest": forms.SelectMultiple(),
        }

        labels = {
            "start_date": "Start Date",
            "total": "Total ($)",
            "link": "FaceBook URL Link",
            "guest": "Guests (*to select multiple guests hold ctr and click*)"
        }

        # CANT GET THE PREPREND TEXT TO WORK TO SHOW DOLLAR SIGN BEFORE INPUT
        # Layout('total',
        #     PrependedText('total', '$')
        # )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['guest'].queryset = Contact.objects.all().filter(consultant__id=user.id)
        self.fields['host'].queryset = Contact.objects.all().filter(consultant__id=user.id)

