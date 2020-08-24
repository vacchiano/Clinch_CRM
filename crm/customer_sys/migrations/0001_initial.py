# Generated by Django 2.2 on 2020-08-14 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(blank=True, max_length=45)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=45)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('last_contact', models.DateField(blank=True)),
                ('bg_info', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('Cold', 'Cold'), ('Warm', 'Warm'), ('Party', 'Interested in Party'), ('Consultant', 'Interested in Consulting'), ('Host', 'Hosted Party'), ('Joined', 'Joined Team')], default='Cold', max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField()),
                ('link', models.CharField(blank=True, max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parties', to=settings.AUTH_USER_MODEL)),
                ('guest', models.ManyToManyField(related_name='parties_attending', to='customer_sys.Contact')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parties_hosting', to='customer_sys.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('body', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='customer_sys.Contact')),
            ],
        ),
    ]
