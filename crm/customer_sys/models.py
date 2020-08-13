from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    phone = models.CharField(max_length=45)
    address = models.CharField(max_length=255)
    last_contact = models.DateField()
    bg_info = models.TextField()
    status = models.CharField(max_length=255)
    
    consultant = models.ForeignKey(User, related_name="contacts", on_delete=models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_created=True)

    # notes = all the users notes
    # parties_hosting = parties that this customer is hosting
    # parties_attending = parties this customer is a guest at

class Note(models.Model):
    body = models.TextField()
    contact = models.ForeignKey(Contact, related_name="notes", on_delete=models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_created=True)

class Party(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    link = models.CharField(max_length=255)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_created=True)

    host = models.ForeignKey(Contact, related_name="parties_hosting", on_delete=models.CASCADE)
    guest = models.ManyToManyField(Contact, related_name="parties_attending")