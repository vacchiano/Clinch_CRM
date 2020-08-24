from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):

    status_choices = (
        ("Cold", "Cold"),
        ("Warm", "Warm"),
        ("Party", "Interested in Party"),
        ("Consultant", "Interested in Consulting"),
        ("Host", "Hosted Party"),
        ("Joined", "Joined Team")
    )

    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True)
    address = models.CharField(max_length=255, blank=True)
    last_contact = models.DateField(blank=True, null=True)
    bg_info = models.TextField(blank=True)
    status = models.CharField(max_length=255, choices=status_choices, default="Cold")
    
    consultant = models.ForeignKey(User, related_name="contacts", on_delete=models.CASCADE, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.first_name + " " + self.last_name)

    # notes = all the users notes
    # parties_hosting = parties that this customer is hosting
    # parties_attending = parties this customer is a guest at

class Note(models.Model):
    body = models.TextField()
    contact = models.ForeignKey(Contact, related_name="notes", on_delete=models.CASCADE, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Party(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    link = models.CharField(max_length=255, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    host = models.ForeignKey(Contact, related_name="parties_hosting", on_delete=models.CASCADE, blank=True)
    guest = models.ManyToManyField(Contact, related_name="parties_attending", blank=True)

    consultant = models.ForeignKey(User, related_name="parties", on_delete=models.CASCADE, blank=True)