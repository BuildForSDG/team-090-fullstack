# Generated by Django 3.0.6 on 2020-06-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullstack', '0006_auto_20200630_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='picture',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]