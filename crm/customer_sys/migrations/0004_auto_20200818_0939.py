# Generated by Django 2.2 on 2020-08-18 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_sys', '0003_auto_20200818_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_contact',
            field=models.DateField(blank=True, null=True),
        ),
    ]
