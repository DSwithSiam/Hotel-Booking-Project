# Generated by Django 4.2.6 on 2024-01-18 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]