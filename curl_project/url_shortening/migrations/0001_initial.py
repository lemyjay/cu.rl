# Generated by Django 4.2.11 on 2024-05-16 16:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlotTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_slot', models.IntegerField(default=6)),
                ('max_records', models.BigIntegerField(default=68719476736)),
                ('records_used', models.BigIntegerField(default=0)),
                ('slots_left', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='URL',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('original_url', models.URLField(max_length=2000)),
                ('shortened_slug', models.CharField(max_length=50, unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('customized', models.BooleanField(default=False, help_text='Designates whether the shortened slug is customized or not.', verbose_name='Customized URL')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='Active status')),
                ('expired', models.BooleanField(default=False, help_text='Designates whether the shortened slug is expired or not.', verbose_name='Expiry status')),
            ],
        ),
    ]
