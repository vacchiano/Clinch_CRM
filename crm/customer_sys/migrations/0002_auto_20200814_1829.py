# Generated by Django 2.2 on 2020-08-14 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_sys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='guest',
            field=models.ManyToManyField(blank=True, related_name='parties_attending', to='customer_sys.Contact'),
        ),
    ]