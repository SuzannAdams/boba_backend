# Generated by Django 3.0.4 on 2020-03-12 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boba', '0002_meet_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='date',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meet',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]