# Generated by Django 3.0.6 on 2020-06-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullstack', '0005_auto_20200628_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='picture',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]